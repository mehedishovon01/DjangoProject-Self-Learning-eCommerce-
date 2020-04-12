from django.db import models
from django.utils import timezone
from django.conf import settings
from Products.models import Product
from django.db.models.signals import pre_save, post_save, m2m_changed

# Get User from the Model
User = settings.AUTH_USER_MODEL


class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        query_set = self.get_queryset().filter(id=cart_id)
        if query_set.count() == 1:
            new_obj = False
            # print("Cart ID Exists")
            cart_obj = query_set.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    products = models.ManyToManyField(Product, blank=True)
    sub_total = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)
    total_price = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)
    timestamp = models.DateTimeField(default=timezone.now)

    objects = CartManager()

    def __str__(self):
        return str(self.id)


def m2m_cart_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        products = instance.products.all()
        total_price = 0
        for x in products:
            total_price += x.price
        if instance.sub_total != total_price:
            instance.sub_total = total_price
            instance.save()


m2m_changed.connect(m2m_cart_receiver, sender=Cart.products.through)


def pre_save_cart_receiver(sender, instance, *args, **kwargs):
    instance.total_price = instance.sub_total + 10


pre_save.connect(pre_save_cart_receiver, sender=Cart)

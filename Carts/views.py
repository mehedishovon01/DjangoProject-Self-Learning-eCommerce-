from django.shortcuts import render


def carts(request):
    # print(request.session)
    # print(dir(request.session))
    key = request.session.session_key
    print(key)
    return render(request, 'carts/carts.html')
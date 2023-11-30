from django.shortcuts import render

from app.models import *


def timkiem(request):
    categories = Category.objects.filter(is_sub=False)  # lay cac damh muc lon
    slide_hidden = "hidden"
    fixed_height = "20px"
    # check xem phải admin không
    check_staff = request.user
    if check_staff.is_staff:
        print('admin')
        show_manage = 'show'
    else:
        print('not admin')
        show_manage = 'none'

    if request.user.is_authenticated: # neu da xac thuc
        user_not_login = "none"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "none"

    print("abcxyz")
    if request.method == "POST":
        print("vao day")
        key = request.POST["searched"]
        print(key)
        product_rq = Product.objects.filter(name__contains=key)
        print(product_rq)
        

    return render(request, "app/timkiem.html",
                  {'categories': categories,
                   'user_login': user_login,
                   'user_not_login': user_not_login,
                   'product_rq': product_rq,
                   'key': key,
                   'slide_hidden': slide_hidden,
                   'fixed_height': fixed_height,
                   'show_manage': show_manage,
                   }
                   )

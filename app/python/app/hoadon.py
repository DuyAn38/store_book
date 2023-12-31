from django.contrib import messages
from django.shortcuts import render

from app.models import *


def hoadon(request):
    slide_hidden = "hidden"
    fixed_height = "20px"
    check_staff = request.user
    if check_staff.is_staff:
        print('admin')
        show_manage = 'show'
    else:
        print('not admin')
        show_manage = 'none'
    # lấy các sản phẩm
    total_all = 0
    count = 0
    if request.user.is_authenticated:
        customer = request.user
        items = Cart.objects.filter(user=customer)
        user_not_login = "none"
        user_login = "show"
        for item in items:
            item.total = item.product.price * item.quantity
            total_all += item.product.price * item.quantity
            count += item.quantity
    else:
        order = None
        items = []
        user_not_login = "show"
        user_login = "none"

# Xử lý chính
    id = request.GET.get('id', '')
    print("lấy id của address: " + id)
     # Lấy tham số 'paymentMethod' từ URL
    payment = request.GET.get('paymentMethod')
    print("lấy id của: " + payment)

    address = Adress.objects.filter(id=id)
    address_data = address.values()
    try:
        single_address = address.get()
        # Lấy các trường cụ thể, ví dụ lấy tên người dùng và địa chỉ
        city = single_address.city
        address_sate = single_address.adress
        name = single_address.name_user
        mobile = single_address.mobile
        district = single_address.district
        commune = single_address.commune
        order = Order(customer=customer, address=single_address, complete=False, payment=payment)
        order.save()

        for item in items:
            items_order = OrderItem(product=item.product, order=order, quantity=item.quantity, total= item.product.price * item.quantity)
            items_order.save()
            # item.product.count_order += 1

        products = OrderItem.objects.filter(order=order)
        for item in products:
            item.total = item.product.price * item.quantity

        items.delete()
    except Adress.DoesNotExist:
        # Xử lý trường hợp không tìm thấy bản ghi
        pass

    print(name, city, address_sate, mobile, district, commune)
    for item in items:
        print(item)

    context = {'items': items,
               'products': products,
               'total_all': total_all,
               'count': count,
               'user_login': user_login,
               'user_not_login': user_not_login,
               'messages': messages,
               'slide_hidden': slide_hidden,
               'fixed_height': fixed_height,
               'show_manage': show_manage,
               'payment': payment,
               }
    return render(request, 'app/hoadon.html', context)

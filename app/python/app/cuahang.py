
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from app.models import *


def cuahang(request):
    user = request.user
    if user.is_staff:
        print('admin')
        show_manage = 'show'
    else:
        print('not admin')
        show_manage = 'none'
    products = Product.objects.all()
    paginator = Paginator(products, 8)  # Chia danh sách sản phẩm thành các trang, mỗi trang có 8 sản phẩm
    recent_products = Product.objects.order_by('time')[:8]
    page_number = request.GET.get('page')  # Lấy số trang từ tham số truy vấn URL
    page = paginator.get_page(page_number)  # Lấy trang hiện tại
    total_all = 0
    count = 0
    if request.user.is_authenticated:
        customer = request.user
        items = Cart.objects.filter(user=customer)
        user_not_login = "none"
        user_login = "show"
        for item in items:
            if item.product is not None and hasattr(item.product, 'price'):
                item.total = item.product.price * item.quantity
                total_all += item.product.price * item.quantity
                count += item.quantity
            else:
                item.total = 0
    else:
        items = []
        user_not_login = "show"
        user_login = "none"

    categories = Category.objects.filter(is_sub=False)  # lay cac damh muc lon
    active_category = request.GET.get('category', '')
    context = {'products': products,
               'recent_products': recent_products,
               'items': items,
               'total_all': total_all,
               'count': count,
               'user_login': user_login,
               'user_not_login': user_not_login,
               'categories': categories,
               'active_category': active_category,
               'show_manage': show_manage,
               'page': page,
               }
    return render(request, 'app/cuahang.html', context)

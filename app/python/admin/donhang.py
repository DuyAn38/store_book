from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from app.models import *

def donhang(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'admin/donhang.html', context)


def xemdonhang(request):
    id = request.GET.get('id', '')
    order =  get_object_or_404(Order, id=id)
    print('id order: ')
    print(id)
    order_items = {}
    total = 0
    items = OrderItem.objects.filter(order=order)
    order_items[order] = items
    total_order_amount = 0
    for item in items:
        total += item.total

    context={'order': order,
             'order_items': order_items,
             'items': items,
             'total': total,
             }
    return render(request, 'admin/xemdonhang.html', context)

def xoadonhang(request):
    id = request.GET.get('id', '')  # lấy id khi người dùng vlick vào sản phẩm nào đó
    order = get_object_or_404(Order, id=id)
    print(order)
    items = OrderItem.objects.filter(order=order)
    print(items)
    if request.method == 'POST':
        items.delete()
        order.delete()
        messages.success(request, 'Xóa đơn hàng thành công')
        return redirect('quanlydonhang')
    context = {'product': order}

    return render(request, 'admin/xoadonhang.html', context)
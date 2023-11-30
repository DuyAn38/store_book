from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from app.models import Product
from app.models import *


def sanpham(request):
    products = Product.objects.all()
    form = AddProduct()
    context = {'products': products}
    return render(request, 'admin/sanpham.html', context)

def themsanpham(request):
    form = AddProduct()
    if request.method == 'POST':
        form = AddProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(form)
            # Thông báo thành công và chuyển hướng
            messages.success(request, 'thêm sản phẩm thành công!')
            return redirect('sanpham')
        else:
            # Xử lý trường hợp form không hợp lệ
            print(form.errors.as_data())
            print(form.errors)
            count = 0  # Hoặc giá trị mặc định khác tùy ý
    else:
        form = AddProduct()
        count = 0  # Hoặc giá trị mặc định khác tùy ý

    context = {'form': form, 'messages': messages, 'count': count}
    return render(request, 'admin/sanpham_them.html', context)

def xemsanpham(request):
    id = request.GET.get('id', '')  # lấy id khi người dùng click vào sản phẩm nào đó
    user = request.user
    print(user)
    products = get_object_or_404(Product, id=id)
    categories_product = products.category.values_list('id', flat=True)
    # Lấy danh sách tên danh mục từ danh sách ID
    category_names = Category.objects.filter(id__in=categories_product).values_list('name', flat=True)
    print(category_names)
    # Chuyển danh sách tên thành danh sách Python
    category_names_list = list(category_names)
    categories = Category.objects.filter(is_sub=True)  # lay cac damh muc lon
    context = {'product': products,
               'category_names_list': category_names_list,
               }
    return render(request, 'admin/sanpham_xem.html', context)


def suasanpham(request):
    id = request.GET.get('id', '')  # lấy id khi người dùng click vào sản phẩm nào đó
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = AddProduct(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'sửa sản phẩm thành công!')
            return redirect('sanpham')
    form = AddProduct(instance=product,
                      initial={'name': product.name,
                               'category': product.category.values_list('id', flat=True),
                               'price': product.price,
                               'describe': product.describe,
                               'image': product.image})

    context = {'product': product,
               'form': form}
    return render(request, 'admin/sanpham_sua.html', context)

# def xoasanpham(request):
#     id = request.GET.get('id', '')  # lấy id khi người dùng click vào sản phẩm nào đó
#     product = get_object_or_404(Product, id=id)
#     if request.method == 'POST':
#         product.delete()
#         messages.success(request, 'Xóa sản phẩm thành công')
#         return redirect('sanpham')
#     context ={'product': product}
#     return render(request, 'admin/xoasanpham.html', context)

def xoasanpham(request, id):
    category = get_object_or_404(Product, id=id)
    Product.objects.filter(id=id).delete()
    return redirect('sanpham')


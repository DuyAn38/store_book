from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from app.models import Category
from app.models import *

def danhmuc(request):
    categories = Category.objects.all()  # lay cac damh muc lon
    context ={'categories': categories}
    return render(request, 'admin/danhmuc.html', context)


def themdanhmuc(request):
    form = AddCategory()
    categories = Category.objects.filter(is_sub=False)
    if request.method == 'POST':
        form = AddCategory(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category saved successfully!')
            return redirect('danhmuc')

    context = {'form': form,
               'messages': messages,}
    return render(request, 'admin/danhmuc_them.html', context)


def suadanhmuc(request):
    id = request.GET.get('id', '')  # lấy id khi người dùng vlick vào sản phẩm nào đó
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        form = AddCategory(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thêm danh mục thành công!')
            return redirect('danhmuc')
    form = AddCategory(instance=category, initial={'sub_category': category.sub_category, 
                                                   'is_sub': category.is_sub,
                                                   'name': category.name, 
                                                   'slug': category.slug, 
                                                   })

    context = {'category': category,
               'form': form}
    return render(request, 'admin/danhmuc_sua.html', context)

def xoadanhmuc(request, id):
    category = get_object_or_404(Category, id=id)
    Category.objects.filter(id=id).delete()
    return redirect('danhmuc')
    

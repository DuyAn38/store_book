from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from app.models import *


def thanhvien(request):
    users = User.objects.all()  # lay cac damh muc lon
    context = {'users': users}
    return render(request, 'admin/thanhvien.html', context)


def themthanhvien(request):
    slide_hidden = "hidden"
    fixed_height = "20px"
    from_register = CreateUserForm()
 
    context = {'from': from_register,
               'slide_hidden': slide_hidden,
               'fixed_height': fixed_height}

    # khi người dùng ấn nút đăng kí
    if request.method == 'POST':
        from_register = CreateUserForm(request.POST)
        if from_register.is_valid(): # kiểm tra đúng yêu cầu thì lưu cái form đó lại
            from_register.save()
            return redirect('quanlythanhvien')
    return render(request, "admin/thanhvien_them.html", context)

def xemthanhvien(request):
    id = request.GET.get('id', '')
    user =  get_object_or_404(User, id=id)
    print('id user: ')
    print(id)
    context={'user': user,
             }
    return render(request, 'admin/sanpham_xem.html', context)


def xoathanhvien(request):
    id = request.GET.get('id', '') 
    user = get_object_or_404(User, id=id)
    print(user)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Xóa thành viên thành công')
        return redirect('quanlythanhvien')
    context = {'user': user}
    return render(request, 'admin/thanhvien_xoa.html', context)




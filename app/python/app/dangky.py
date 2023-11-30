from django.shortcuts import redirect, render
from app.models import CreateUserForm

from app.models import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

def dangky(request):
    slide_hidden = "hidden"
    fixed_height = "20px"
    from_register = CreateUserForm()
    user_not_login = "show"
    user_login = "none"
    none_margin = '0px'
    
    context = {'from': from_register,
               'user_login': user_login,
               'user_not_login': user_not_login,
               'slide_hidden': slide_hidden,
               'fixed_height': fixed_height,
               'none_margin': none_margin,
               }

    # khi người dùng ấn nút đăng kí
    if request.method == 'POST':
        from_register = CreateUserForm(request.POST)
        if from_register.is_valid(): # kiểm tra đúng yêu cầu thì lưu cái form đó lại
            from_register.save()
            return redirect('dangnhap')
    return render(request, "app/dangky.html", context)



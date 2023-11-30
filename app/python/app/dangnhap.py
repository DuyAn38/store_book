from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render


def dangnhap(request):
    slide_hidden = "hidden"
    fixed_height = "20px"
    user_not_login = "show"
    user_login = "none"
    none_margin = '0px'
    
    if request.user.is_authenticated: # neu da xac thuc
        return redirect('trangchu')
    if request.method == 'POST':
        userName = request.POST.get('username')
        passWord = request.POST.get('password')
        user = authenticate(request, username=userName, password=passWord)
        messages.success(request, 'Đăng nhập thành công')
        if user is not None:
            login(request, user)
            return redirect('trangchu')
            
        else:
            messages.error(request, 'Tài khoản hoặc mật khẩu không chính xác.')
    context = {'user_login': user_login,
               'user_not_login': user_not_login,
               'slide_hidden': slide_hidden,
               'fixed_height': fixed_height,
               'none_margin': none_margin,
               }
    return render(request, "app/dangnhap.html", context)

def dangxuat(request):
    logout(request)
    return redirect('dangnhap')
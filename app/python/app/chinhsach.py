from django.shortcuts import render, get_object_or_404, redirect
from app.models import *


def baomat(request):
    check_staff = request.user
    if check_staff.is_staff:
        print('admin')
        show_manage = 'show'
    else:
        print('not admin')
        show_manage = 'none'
    if request.user.is_authenticated:
        
        user_not_login = "none"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "none"
    context = { 
               'user_login': user_login,
               'user_not_login': user_not_login,}
    
    return render(request, 'app/baomat.html', context )

def chinhsachgiaohang(request):
    check_staff = request.user
    if check_staff.is_staff:
        print('admin')
        show_manage = 'show'
    else:
        print('not admin')
        show_manage = 'none'
    if request.user.is_authenticated:
        
        user_not_login = "none"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "none"
    context = { 
               'user_login': user_login,
               'user_not_login': user_not_login }
    
    
    return render(request, 'app/chinhsachgiaohang.html', context )

def doitra(request):
    check_staff = request.user
    if check_staff.is_staff:
        print('admin')
        show_manage = 'show'
    else:
        print('not admin')
        show_manage = 'none'
    if request.user.is_authenticated:
        
        user_not_login = "none"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "none"
    context = { 
               'user_login': user_login,
               'user_not_login': user_not_login }
    
    
    return render(request, 'app/doitra.html', context )

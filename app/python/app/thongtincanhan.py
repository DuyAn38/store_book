from app.python.app.base import show_manage
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import *

from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


def thongtincanhan(request):
    categories = Category.objects.filter(is_sub=False)  # lay cac damh muc lon
    slide_hidden = "hidden"
    fixed_height = "20px"
    check_staff = request.user
    if check_staff.is_staff:
        print('admin')
        show_manage = 'show'
    else:
        print('not admin')
        show_manage = 'none'
    if request.user.is_authenticated:
        user = request.user
        address_infor = Adress.objects.filter(customer=user)
    user_address = None
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['adress']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            mobile = form.cleaned_data['mobile']
            user_address = Adress(customer=request.user, adress=address, city=city, state=state, mobile=mobile)
            user_address.save()
    else:
        form = AddressForm()

    if request.user.is_authenticated:
        customer = request.user
       
        user_not_login = "none"
        user_login = "show"
        
    else:
       
        user_not_login = "show"
        user_login = "none"

    context = {'user': user,
               'form': form,
               'address_infor': address_infor,
               'user_address': user_address,
               'slide_hidden': slide_hidden,
               'fixed_height': fixed_height,
               'user_not_login': user_not_login,
               'user_login': user_login,
               'categories': categories,   
               'show_manage': show_manage,
               }
    return render(request, 'app/thongtincanhan.html', context)




def suathongtincanhan(request):
    categories = Category.objects.filter(is_sub=False)  # lay cac damh muc lon
    user = request.user
    if request.method == 'POST':

        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.save()
        return redirect('thongtincanhan')
    
    form = CreateUserForm(instance=user, 
                       initial={
                                'last_name': user.last_name, 
                                'first_name': user.first_name,
                                'email': user.email,
                                
                                })
    if request.user.is_authenticated:
        customer = request.user
       
        user_not_login = "none"
        user_login = "show"
        
    else:
       
        user_not_login = "show"
        user_login = "none"
    context = {
        'user_not_login':user_not_login,
        'user_login': user_login,
        'categories': categories, 
        'form': form
               }
    return render(request, 'app/suathongtincanhan.html', context)


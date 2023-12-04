from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from app.models import *


def themdiachi(request):
    categories = Category.objects.filter(is_sub=False)  # lay cac damh muc lon
    check_staff = request.user
    if check_staff.is_staff:
        print('admin')
        show_manage = 'show'
    else:
        print('not admin')
        show_manage = 'none'
    slide_hidden = "hidden"
    fixed_height = "20px"
    form = AddressForm()
    check_staff = request.user

    # Kiểm tra xem người dùng đã đăng nhập chưa
    if isinstance(check_staff, User) and request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['name_user']
            mobile = form.cleaned_data['mobile']
            address = form.cleaned_data['adress']
            city = form.cleaned_data['city']
            district = form.cleaned_data['district']
            commune = form.cleaned_data['commune']

            add_address_user = Adress(customer=check_staff, name_user=user_name, adress=address, city=city, mobile=mobile, district=district, commune=commune)
            print(add_address_user)
            add_address_user.save()
            print('them thanh cong')
            return redirect('thongtincanhan')
        else:
            print(form.errors)
            print('them khong thanh cong')
    if request.user.is_authenticated:
        user_not_login = "none"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "none"
    context = {'form': form,
               'messages': messages,
               'slide_hidden': slide_hidden,
               'fixed_height': fixed_height,
               'categories': categories,  
               'user_not_login':user_not_login,
               'user_login': user_login,
               'show_manage': show_manage,
               }
    return render(request, 'app/themdiachi.html', context)

    
    

def suadiachi(request):
    categories = Category.objects.filter(is_sub=False)  # lay cac damh muc lon
    slide_hidden = "hidden"
    fixed_height = "20px"
    # check xem phải admin không
    check_staff = request.user
    if check_staff.is_staff:
        print('admin')
        show_manage = 'show'
    else:
        print('not admin')
        show_manage = 'none'

    id = request.GET.get('id', '')
    address_user = get_object_or_404(Adress, id=id)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address_user)
        if form.is_valid():
            user_name = form.cleaned_data['name_user']
            mobile = form.cleaned_data['mobile']
            address = form.cleaned_data['adress']
            city = form.cleaned_data['city']
            district = form.cleaned_data['district']
            commune = form.cleaned_data['commune']

            address_user.customer = request.user
            address_user.name_user = user_name
            address_user.adress = address
            address_user.city = city
            address_user.mobile = mobile
            address_user.district = district
            address_user.commune = commune
            print(address_user)
            address_user.save()
            print('Address saved successfully!')
            return redirect('thongtincanhan')
        else:
            print("Form is not valid")
    else:
        form = AddressForm(instance=address_user)
    if request.user.is_authenticated:
        user_not_login = "none"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "none"
    context = {'form': form,
               'slide_hidden': slide_hidden,
               'fixed_height': fixed_height,
               'categories': categories,  
               'user_not_login':user_not_login,
               'user_login': user_login,
               'show_manage': show_manage,
               }
    return render(request, 'app/suadiachi.html', context)


def xoadiachi(request, id):
    order = get_object_or_404(Adress, id=id)
    order.delete()
    messages.warning(request, 'xóa địa chỉ thành công')
    return redirect('thongtincanhan')


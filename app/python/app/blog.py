from django.shortcuts import render, get_object_or_404, redirect
from app.models import *


def blog(request):
    categories = Category.objects.filter(is_sub=False)  # lay cac damh muc lon
    if request.user.is_authenticated:
        user_not_login = "none"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "none"
    
    context = {
        'user_not_login':user_not_login,
        'user_login': user_login,
        'categories': categories,   

    }
    
    return render(request, 'app/blog.html',context )

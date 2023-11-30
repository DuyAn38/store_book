from django.shortcuts import render


def basea(request):
    context ={}
    return render(request, 'admin/basea.html', context)

def bangthongtin(request):
    context ={}
    return render(request, 'admin/bangthongtin.html', context)

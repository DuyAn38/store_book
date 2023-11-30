from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.utils import timezone
from rest_framework import serializers
from django.contrib.auth.forms import UserCreationForm

class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_categories', null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200, null=True)
    slug = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name
    



class Adress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name_user = models.CharField(max_length=200, null=True)
    adress = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    mobile = models.CharField(max_length=200, null=True)
    district = models.CharField(max_length=200, null=True)
    commune = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name_user


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)                                  
    category = models.ManyToManyField(Category, related_name='product_category')
    price = models.IntegerField(null=False,default=0)
    price_sale = models.IntegerField(null=False,default=0)
    describe = models.CharField(max_length=300, null=True)
    image = models.ImageField(null=True, blank=True)       
    author = models.CharField(max_length=200, null=True)
    numberofpages = models.IntegerField(null=False,default=0)
    publisher = models.CharField(max_length=300, null=True, blank=False)
    publishingyear = models.IntegerField(default=0, null=False, blank=False) 
    count = models.IntegerField(null=False, default=0)
    time = models.DateTimeField(auto_now_add=True, blank=True, null= True)
    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
  

#giỏ hàng
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    total = models.FloatField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

#đặt hàng
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.ForeignKey(Adress, on_delete=models.SET_NULL, null=True, blank=True)
    date_order = models.DateTimeField(auto_now_add=True)
    payment = models.CharField(max_length=100, null=True, blank=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    def __str__(self):
        return str(self.id)
    @property
    def get_cart_item(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        # lấy hết tất cả tiền của các mặt hàng
        total = sum([item.get_total for item in orderitems])
        return total
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    total = models.FloatField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    # lấy tiền của mỗi sản phẩm
    @property
    def get_total(self):
        return self.total


#them danh muc
class AddCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['sub_category', 'is_sub', 'name', 'slug']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

#them san pham
class AddProduct(forms.ModelForm):
    # count = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'price_sale', 'describe', 'image','count', 'author', 'numberofpages','publisher','publishingyear' ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'describe': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 150px'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'count': forms.TextInput(attrs={'class': 'form-control'}),
            'price_sale': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input, d-flex'}),
            'author' :  forms.TextInput(attrs={'class': 'form-control'}),
            'numberofpages' : forms.TextInput(attrs={'class': 'form-control'}),
            'publisher' : forms.TextInput(attrs={'class': 'form-control'}),  
            'publishingyear' : forms.TextInput(attrs={'class': 'form-control'}),
            
        }





#themdiachi
class AddressForm(forms.ModelForm):
    class Meta:
        model = Adress
        fields = ['customer', 'name_user', 'adress', 'city', 'mobile', 'district', 'commune']
        widgets = {
            'customer': forms.TextInput(attrs={'class': 'form-control'}),
            'name_user': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'commune': forms.TextInput(attrs={'class': 'form-control'}),
            'adress': forms.TextInput(attrs={'class': 'form-control'}),

        }

# tao tai khoan
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
        }



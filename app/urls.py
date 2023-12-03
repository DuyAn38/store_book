from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('base/', views.base, name="base"),
    path('', views.trangchu, name="trangchu"),
    path('timkiem/', views.timkiem, name="timkiem"),
    path('blog/', views.blog  , name="blog"),
    path('lienhe/', views.lienhe  , name="lienhe"),
    path('updateItem/', views.updateItem  , name="updateItem"),
    path('baomat/', views.baomat  , name="baomat"),
    path('doitra/', views.doitra  , name="doitra"),
    path('chinhsachgiaohang/', views.chinhsachgiaohang  , name="chinhsachgiaohang"),
  

    path('giohang/', views.giohang  , name="giohang"),
    path('muahang/', views.muahang  , name="muahang"),
    path('hoadon/', views.hoadon  , name="hoadon"),
    path('donhangcuatoi/', views.donhangcuatoi  , name="donhangcuatoi"),
    path('delete_myOrder/', views.deletemyOrder  , name="delete_myOrder"),

    
    path('dangnhap/', views.dangnhap  , name="dangnhap"),
    path('dangxuat/', views.dangxuat, name="dangxuat"),
    path('dangky/', views.dangky  , name="dangky"),
    

    path('thongtincanhan/', views.thongtincanhan , name="thongtincanhan" ),
    path('suathongtincanhan/', views.suathongtincanhan , name="suathongtincanhan" ),
    path('themdiachi/', views.themdiachi , name="themdiachi" ),
    path('suadiachi/', views.suadiachi , name="suadiachi" ),
    path('xoadiachi/', views.xoadiachi , name="xoadiachi" ),
    path('doimatkhau/', views.doimatkhau , name="doimatkhau" ),
    

    path('chitiet/', views.chitiet , name="chitiet" ),

    path('hang/', views.phanloai , name="phanloai" ),
    path('cuahang/', views.cuahang , name="cuahang"),

    # phan admin
    path('basea/', views.basea , name="basea" ),
    path('bangthongtin/', views.bangthongtin , name="bangthongtin" ),

    path('danhmuc/', views.danhmuc , name="danhmuc" ),
    path('themdanhmuc/', views.themdanhmuc , name="themdanhmuc" ),
    path('suadanhmuc/', views.suadanhmuc , name="suadanhmuc" ),
    path('xoadanhmuc/<int:id>/', views.xoadanhmuc , name="xoadanhmuc" ),

    path('sanpham/', views.sanpham , name="sanpham" ),
    path('themsanpham/', views.themsanpham , name="themsanpham" ),
    path('xemsanpham/', views.xemsanpham , name="xemsanpham" ),
    path('suasanpham/', views.suasanpham , name="suasanpham" ),
    path('xoasanpham/<int:id>/', views.xoasanpham , name="xoasanpham" ),

    path('thanhvien/', views.thanhvien , name="thanhvien" ),
    path('themthanhvien/', views.themthanhvien , name="themthanhvien" ),
    path('xemthanhvien/', views.xemthanhvien , name="xemthanhvien" ),
    path('xoathanhvien/<int:id>/', views.xoathanhvien , name="xoathanhvien" ),

    path('donhang/', views.donhang , name="donhang" ),
    path('xemdonhang/', views.xemdonhang , name="xemdonhang" ),
    path('xoadonhang/<int:id>/', views.xoadonhang , name="xoadonhang" ),
    #API

]




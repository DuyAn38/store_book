# from itertools import product
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from .models import *
# app
from .python.app.base import *
from .python.app.updateItem import updateItem
from .python.app.timkiem import timkiem
from .python.app.lienhe import lienhe
from .python.app.chinhsach import baomat,chinhsachgiaohang,doitra


from .python.app.giohang import giohang
from .python.app.muahang import muahang
from .python.app.hoadon import hoadon
from .python.app.donhangcuatoi import donhangcuatoi,deletemyOrder

from .python.app.dangky import dangky
from .python.app.dangnhap import dangnhap,dangxuat
from .python.app.blog import blog
from .python.app.thongtincanhan import thongtincanhan,suathongtincanhan,doimatkhau
from .python.app.diachi import themdiachi,suadiachi,xoadiachi
from .python.app.chitiet import chitiet

from .python.app.phanloai import phanloai
from .python.app.cuahang import cuahang

# admin
from .python.admin.manage import basea,bangthongtin

from .python.admin.danhmuc import danhmuc,themdanhmuc,suadanhmuc,xoadanhmuc

from .python.admin.sanpham import sanpham,themsanpham,xemsanpham,suasanpham,xoasanpham

from .python.admin.thanhvien import thanhvien,themthanhvien,xemthanhvien,xoathanhvien

from .python.admin.donhang import donhang,xemdonhang,xoadonhang


#API







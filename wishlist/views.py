from tkinter import S
from django.shortcuts import render
from wishlist.models import BarangWishlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Divany'
    }
    return render(request, "wishlist.html", context)

def export_to_xml(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type = "application/xml")

def export_to_json(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type = "application/json")

def export_xml_id(request, id):
    data = BarangWishlist.objects.filter(pk = id)
    return HttpResponse(serializers.serialize("xml", data), content_type = "application/xml")

def export_json_id(request, id):
    data = BarangWishlist.objects.filter(pk = id)
    return HttpResponse(serializers.serialize("json", data), content_type = "application/json")
    

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import ImgProductUpload
from app2.models import Product


def get_all_products(request):

    order_list = Product.objects.filter().all()
    return render(request, 'app4/all_products.html', {'context': order_list})


def upload_img_product(request, pk):

    if request.method == 'POST':
        form = ImgProductUpload(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data['img']
            product = Product.objects.filter(id=pk).first()
            product.img = img
            product.save()
    else:
        form = ImgProductUpload()
    return render(request, 'app4/upload_img_product.html', {"form": form})

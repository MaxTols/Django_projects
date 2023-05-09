from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    sort_phone = request.GET.get('sort')
    if sort_phone == 'min_price':
        phones = phones.order_by('price')
    elif sort_phone == 'max_price':
        phones = phones.order_by('-price')
    elif sort_phone == 'name':
        phones = phones.order_by('name')
    context = {
        'phones': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    context = {
        'phone': phone,
    }
    return render(request, template, context)

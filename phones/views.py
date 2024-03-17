from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', None)
    if sort == 'max_price':
        phone_objects = Phone.objects.order_by('-price')
    elif sort == 'min_price':
        phone_objects = Phone.objects.order_by('price')
    elif sort == 'name':
        phone_objects = Phone.objects.order_by('name')
    else:
        phone_objects = Phone.objects.all()
    phones = list(phone_objects)
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_object = Phone.objects.get(slug=slug)
    phone = phone_object
    context = {
        'phone': phone
    }
    return render(request, template, context)

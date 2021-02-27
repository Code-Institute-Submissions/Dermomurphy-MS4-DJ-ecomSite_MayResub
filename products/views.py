from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Brewery

# Create your views here.

def all_products(request):
    """ A View to show all products, including sorting and search queries """
    products = Product.objects.all()
    query = None
    breweries = None
    styles = None
    sort = None
    direction = None

    request.session.set_test_cookie()

    if request.GET:
        if 'sort' in request.GET:
            sortkey =request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction =='desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'styles' in request.GET:
            styles = request.GET['styles'].split(",")
            products = products.filter(style__in=styles)
            

        if 'brewery' in request.GET:
            breweries = request.GET['brewery'].split(",")
            products = products.filter(brewery__country__in=breweries)
            breweries = Brewery.objects.filter(country__in=breweries)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did not enter any search Criteria")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
    
    current_sorting = f'{sort}_{direction}'



    context = {
        'products': products,
        'search_term': query,
        'current_breweries': breweries,
        'current_sorting': current_sorting,
    }


    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A View to show a specific product details"""
    product = get_object_or_404(Product, pk=product_id)

    if request.session.test_cookie_worked():
        print("The test cookie worked!!!")
        # request.session.delete_test_cookie()

    context = {
        'product': product,

    }

    return render(request, 'products/product_detail.html', context)
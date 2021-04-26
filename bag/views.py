from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from django.contrib.sessions.models import Session
from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request,item_id):
    """ Add a quantity of the specified product to the shopping bag """
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    volume = None
    if 'product_volume' in request.POST:
            volume = request.POST['product_volume']
    
    #if Bag in session use it , otherwise create one
    bag = request.session.get('bag', {})

    if volume:
            if item_id in list(bag.keys()):
                    if volume in bag[item_id]['items_by_volume'].keys():
                            bag[item_id]['items_by_volume'][volume]+= quantity
                    else:
                            bag[item_id]['items_by_volume'][volume] = quantity
            else:
                    bag[item_id] = {'items_by_volume': {volume: quantity}}
    else:           


        if item_id in list(bag.keys()):
                bag[item_id] += quantity
                messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
                bag[item_id] = quantity
                messages.success(request, f'Added{product.name} to your bag')
        
      # overwite variable with updated session  
    request.session['bag'] = bag
    
    return redirect(redirect_url)


def adjust_bag(request,item_id):
    """ Add a quantity of the specified product to the specific amount """

    quantity = int(request.POST.get('quantity'))
    volume = None
    if 'product_volume' in request.POST:
            volume = request.POST['product_volume']
    
    #if Bag in session use it , otherwise create one
    bag = request.session.get('bag', {})

    if volume:
          if quantity > 0:
                  bag[item_id]['items_by_volume'][volume] = quantity
          else:
                del bag[item_id]['items_by_volume'][volume]
                if not bag[item_id]['items_by_volume']:
                        bag.pop(item_id)
    else:           


        if quantity > 0:
                bag[item_id] = quantity
        else:
                bag.po(item_id)
        
      # overwite variable with updated session  
    request.session['bag'] = bag
    # redirect back to view bag 
    return redirect(reverse('view_bag'))

def remove_from_bag(request,item_id):
    """ Remove Item from Shopping Bag"""

    try:
        volume = None
        if 'product_volume' in request.POST:
                volume = request.POST['product_volume']
        
        #if Bag in session use it , otherwise create one
        bag = request.session.get('bag', {})

        if volume:
                del bag[item_id]['items_by_volume'][volume]
                if not bag[item_id]['items_by_volume']:
                        bag.pop(item_id)

                
        else:           

                bag.pop(item_id)
                
        # overwite variable with updated session  
        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
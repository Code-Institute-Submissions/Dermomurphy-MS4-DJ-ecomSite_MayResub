from django.http import HttpResponse
from .models import Order, OrderLineItem
from products.models import Product
import json
import time



class StripeWH_Handler:
    """ Handle Stripe Webhooks"""

    def __init__(self,request):
        self.request = request

    def handle_event(self, event):
        """ Handle Generic unknown Webhook events from stripe"""

        return HttpResponse(
            content=f'Webhook Received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """ Handle payment_intent.succeded webhook from stripe"""
        intent = event.data.object
        pid = intent.id 
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.data.charges[0].amount / 100, 2)

        # clean shipping details data

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None
        
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=shipping_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country_name__iexact=shipping_details.country,
                    postcode__iexact=shipping_details.postal_code,
                    town_or_city__iexact=shipping_details.city,
                    street_address1__iexact=shipping_details.line1,
                    street_address2__iexact=shipping_details.line2,
                    county__iexact=shipping_details.county,
                    grand_total = grand_total,
                    original_bag=bag,
                    stripe_pid = pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt+=1
                time.sleep(1)
        if order_exists :
                   
                return HttpResponse(
                    content=f'Webhook Received: {event["type"]} | SUCCESS: Verified order already in database',
                    status=200
                )


        else:
            order = None
            try:          
                order= Order.objects.create(
                            full_name=shipping_details.name,
                            email=shipping_details.email,
                            phone_number=shipping_details.phone,
                            country_name=shipping_details.country,
                            postcode=shipping_details.postal_code,
                            town_or_city=shipping_details.city,
                            street_address1=shipping_details.line1,
                            street_address2=shipping_details.line2,
                            county=shipping_details.county,
                            original_bag = bag,
                            stripe_pid = pid,
                        )
                for item_id, item_data in json.loads(bag).items():
                
                        product = Product.objects.get(id=item_id)
                        if isinstance(item_data, int):
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=item_data,
                            )
                            order_line_item.save()
                        else:
                            for size, quantity in item_data['items_by_volume'].items():
                                order_line_item = OrderLineItem(
                                    order=order,
                                    product=product,
                                    quantity=quantity,
                                    product_volume=volume,
                                )
                                order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(content=f'Webhook Received: {event["type"]} | Error: {e}', status = 500)

        return HttpResponse(
            content=f'Webhook Received: {event["type"]} | Success Creatted order in Webhook',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """ Handle payment_intent.payment_failed webhook  from stripe"""

        return HttpResponse(
            content=f'Webhook Received: {event["type"]}',
            status=200
        )
    
    

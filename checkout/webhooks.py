from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from checkout.webhook_handler import StripeWH_Handler

import stripe

@require_POST
@csrf_exempt

def webhook(request):
    """ Listen for webhooks from Stripe """
    payload = request.body
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
        payload,sig_header, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        # Exception
        return HttpResponse(status=400)
    
   # Set up a webhook handler
    handler = StripeWH_Handler(request)

   #map webhook events to relevant handler functions
    çevent_map = {
       'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
       'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
        }
 
   # get the webhook type from stripe
    event_type = event['type']

    # if there a handler for it, get it from the event map
    # use the generic one by default
    event_handler = event_map.get(event_type, handler.handle_event)

    #call the even handler with the event
    response = event_handler(event)
    return response
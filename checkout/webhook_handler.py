from django.http import HttpResponse


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
        print(intent)

        return HttpResponse(
            content=f'Webhook Received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """ Handle payment_intent.payment_failed webhook  from stripe"""

        return HttpResponse(
            content=f'Webhook Received: {event["type"]}',
            status=200
        )
    
    

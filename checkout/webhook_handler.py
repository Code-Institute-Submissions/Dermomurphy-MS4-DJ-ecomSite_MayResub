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

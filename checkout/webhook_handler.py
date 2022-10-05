from urllib import request
from django.http import HttpResponse


class StripieWH_Handler:
    '''Handle Stripe Webhooks'''

    def __init__(self):
        self.request = request

    def handle_event(self, event):
        '''Handle a generic/unknown/unexpected webhook event'''

        return HttpResponse(
            content=f'Webhook recived: {event["type"]}',
            status=200
        )

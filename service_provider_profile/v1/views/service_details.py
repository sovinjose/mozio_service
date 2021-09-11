from decimal import Decimal
from django.http import JsonResponse
from django.views.generic import View

from ...models import ProviderLocation, ProviderProfile
from .utils import error_message


class GetProviderServiceDetails(View):

    def get(self, request):
        print (request.GET)
        longitude = request.GET.get('longitude')
        latitude= request.GET.get('latitude')
        print (Decimal(longitude), Decimal(latitude))
        if not longitude or  not latitude:
            message =  "longitude or latitude ismissing"
            return JsonResponse(error_message(message), status=400)
        
        items = ProviderLocation.objects.filter(longitude__range=(Decimal(longitude),Decimal(longitude)),
                                                latitude__range=(Decimal(latitude),Decimal(latitude))).\
            select_related('profile')
        items_data = []
        for item in items:
            items_data.append({
                'profile_name': item.profile.name,
                'location_name': item.location_name,
                'longitude': item.longitude,
                'latitude': item.latitude,
                'price': item.price
            })
        data = {
            'items': items_data,
            'count': len(items_data)
        }
        return JsonResponse(data, status=200)


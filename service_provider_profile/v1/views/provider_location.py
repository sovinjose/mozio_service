"""
"""
import json
from django.http import JsonResponse
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from ...models import ProviderLocation, ProviderProfile
from .utils import error_message, validate_provider_location, PROVIDER_LOCATION


@method_decorator(csrf_exempt, name='dispatch')
class ProviderLocationView(View):
    """
    """

    def get(self, request):
        """
        :param request:
        :return:
        """
        try:
            items_count = ProviderLocation.objects.count()
            items = ProviderLocation.objects.all()
        except Exception as e:
            message =  f"Failes to get Profile, Error: {e}"
            return JsonResponse(error_message(message), status=500)
        items_data = []
        for item in items:
            items_data.append({
                'profile_pk': item.profile.pk,
                'location_name': item.location_name,
                'longitude': item.longitude,
                'latitude': item.latitude,
                'price': item.price
            })

        data = {
            'items': items_data,
            'count': items_count,
        }
        return JsonResponse(data, status=200)


    def post(self, request):
        """
        :param request:
        :return:
        """
        try:
            data = json.loads(request.body.decode("utf-8"))
        except Exception as e:
             message = "Failes to create Location info, Error: json decode error"
             return JsonResponse(error_message(message), status=400)
        status , product_data = validate_provider_location(data)
        if not status:
            return JsonResponse(error_message(product_data), status=400)
        try:
            profile_pk = data.get('profile_pk')
            profile_obj = ProviderProfile.objects.get(id=profile_pk)
            product_data['profile'] = profile_obj
            profile = ProviderLocation.objects.create(**product_data)
        except ObjectDoesNotExist as e:
            error = {
            'Error': {'message': f'Profile {profile_pk} does not exist'}
            }
            return JsonResponse(error, status=404)
        except Exception as e:
            message = f"Failes to create Profile, Error: {e}"
            return JsonResponse(error_message(message), status=400)

        data = {
            "message": f"New profile added with id: {profile.id}"
        }
        return JsonResponse(data, status=201)


@method_decorator(csrf_exempt, name='dispatch')
class ProviderLocationUpdateView(View):

    def get(self, request, pk):
        try:
            item = ProviderLocation.objects.get(pk=pk)
            data  = {
                'profile_pk': item.profile.pk,
                'location_name': item.location_name,
                'longitude': item.longitude,
                'latitude': item.latitude,
                'price': item.price
            }
            return JsonResponse(data, status=200)
        except ObjectDoesNotExist as e:
            message =  f'{pk} does not exist'
            return JsonResponse(error_message(message), status=404)


    def put(self, request, pk, *args, **kwargs):
        try:
            data = json.loads(request.body.decode("utf-8"))
        except Exception as e:
             message = "Failes to create Profile, Error: json decode error"
             return JsonResponse(error_message(message), status=400)
        status , product_data = validate_provider_location(data)
        if not status:
            return JsonResponse(error_message(product_data), status=400)
        try:
            profile_pk = data.get('profile_pk')
            profile_obj = ProviderProfile.objects.get(id=profile_pk)
            product_data['profile'] = profile_obj
            profile = ProviderLocation.objects.filter(id=pk).update(**product_data)
        except ObjectDoesNotExist as e:
            error = {
            'Error': {'message': f'{pk} does not exist'}
            }
            return JsonResponse(error, status=404)
        except Exception as e:
            message =  f"Failes to create Profile, Error: {e}"
            return JsonResponse(error_message(message), status=400)

        data = {
            "message": f"Updated profile with id: {pk}"
        }
        return JsonResponse(data, status=201)

    def patch(self, request, pk):
        """
        :param request:
        :param pk:
        :return:
        """
        data = json.loads(request.body.decode("utf-8"))
        try:
            item = ProviderProfile.objects.get(id=pk)
            for i in data.keys():
                if i in PROVIDER_LOCATION:
                    item.i = data.get(i)
            item.save()
        except ObjectDoesNotExist as e:
            message =  f"{pk} does not exist"
            return JsonResponse(error_message(message), status=404)

    def delete(self, request, pk):
        """
        :param request:
        :param pk:
        :return:
        """
        try:
            item = ProviderProfile.objects.get(id=pk)
            item.delete()
        except ObjectDoesNotExist as e:
           message = f'{pk} does not exist'
           return JsonResponse(error_message(message), status=404)

        data = {
            'message': f'profile {pk} has been deleted'
        }
        return JsonResponse(data)


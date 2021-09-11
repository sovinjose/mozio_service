import json
from django.http import JsonResponse
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from ...models import ProviderProfile
from .utils import error_message, validate_payload, MODEL_KEYS


@method_decorator(csrf_exempt, name='dispatch')
class ProvideProfiles(View):
    """
    class to handle Provide Profiles data
    """

    def get(self, request):
        """
        :param request:
        :return:
        """
        try:
            items_count = ProviderProfile.objects.count()
            items = ProviderProfile.objects.all()
        except Exception as e:
            message =  f"Failes to get Profile, Error: {e}"
            return JsonResponse(error_message(message), status=500)
        items_data = []
        for item in items:
            items_data.append({
                'id': item.pk,
                'name': item.name,
                'email': item.email,
                'phone_number': item.phone_number,
                'language': item.language,
                'currency': item.currency
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
             message = "Failes to create Profile, Error: json decode error"
             return JsonResponse(error_message(message), status=400)
        status , product_data = validate_payload(data)
        if not status:
            return JsonResponse(error_message(product_data), status=400)
        try:
            profile = ProviderProfile.objects.create(**product_data)
        except Exception as e:
            message = f"Failes to create Profile, Error: {e}"
            return JsonResponse(error_message(message), status=400)

        data = {
            "message": f"New profile added with id: {profile.id}"
        }
        return JsonResponse(data, status=201)


@method_decorator(csrf_exempt, name='dispatch')
class ProvideProfilesUpdate(View):
    """
    class to handle Provide Profiles updates
    """

    def get(self, request, pk):
        """
        :param request:
        :param pk:
        :return:
        """
        try:
            item = ProviderProfile.objects.get(pk=pk)
            data  = {
                'id': item.pk,
                'name': item.name,
                'email': item.email,
                'phone_number': item.phone_number,
                'language': item.language,
                'currency': item.currency
            }
            return JsonResponse(data, status=200)
        except ObjectDoesNotExist as e:
            message =  f'{pk} does not exist'
            return JsonResponse(error_message(message), status=404)


    def put(self, request, pk):
        """
        :param request:
        :param pk:
        :return:
        """
        try:
            data = json.loads(request.body.decode("utf-8"))
        except Exception as e:
             message = "Failes to create Profile, Error: json decode error"
             return JsonResponse(error_message(message), status=400)
        status , product_data = validate_payload(data)
        if not status:
            return JsonResponse(error_message(product_data), status=400)
        try:
            ProviderProfile.objects.get(id=pk)
            profile = ProviderProfile.objects.filter(id=pk).update(**product_data)
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
                if i in MODEL_KEYS:
                    item.i = data.get(i)
            item.save()
        except ObjectDoesNotExist as e:
            message =  f"{pk} does not exist"
            return JsonResponse(error_message(message), status=404)

    def delete(self, request, pk):
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


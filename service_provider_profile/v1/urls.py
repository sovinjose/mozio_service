from django.urls import path
from .views.provider_profile import ProvideProfiles, ProvideProfilesUpdate
from .views.provider_location import ProviderLocationView, ProviderLocationUpdateView
from .views.service_details import GetProviderServiceDetails


urlpatterns = [
    
    path('profiles', ProvideProfiles.as_view()),
    path('profiles/<int:pk>', ProvideProfilesUpdate.as_view()),
    path('locations', ProviderLocationView.as_view()),
    path('locations/<int:pk>', ProviderLocationUpdateView.as_view()),
    path('service/list', GetProviderServiceDetails.as_view()),
]
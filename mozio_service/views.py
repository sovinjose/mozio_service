from django.shortcuts import redirect


def my_view(request):
    return redirect('provider/v1/profiles')



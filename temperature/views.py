from django.shortcuts import render
from django.http import JsonResponse

def Home(request):
	return render(request, 'temp/home.html',{})

def convert(request):
	temp_in_celcius =float(request.GET.get('temperature_in_celcius'))
	temp_in_fahrenheit= float((temp_in_celcius * 9/5) + 32)
	data = {
        'temp_in_fahrenheit': temp_in_fahrenheit,
    }
	return JsonResponse(data)

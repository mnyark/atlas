from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Record


# Create your views here.

def data(request):
	if request.method == 'GET':
		records = Record.objects.all().values()
		return JsonResponse(list(records), safe=False)

def index(request):
	return render(request, 'index.html')


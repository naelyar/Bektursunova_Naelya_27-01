from django.shortcuts import HttpResponse
import datetime
# Create your views here.
def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello its my project")
def now_date_view(request):
    dt_now = datetime.datetime.now()
    if request.method == 'GET':
        return HttpResponse(dt_now)
def by_view(request):
    if request.method == 'GET':
        return HttpResponse("Goodby user")

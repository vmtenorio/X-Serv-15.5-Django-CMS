from django.shortcuts import render
from cms.models import Pages
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def content(request, rec):
    if request.method != "GET":
        return HttpResponse("Method not allowed", status=405)
    try:
        page = Pages.objects.get(name=rec)
        return HttpResponse(page.page)
    except ObjectDoesNotExist:
        return HttpResponse("Content not found", status=404)

from django.shortcuts import render
from django.http import HttpResponse
from .tasks import send_emails

def index(request):
	send_emails()
	return HttpResponse('Done!')
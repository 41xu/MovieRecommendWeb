from django.shortcuts import render,render_to_response,HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    pass
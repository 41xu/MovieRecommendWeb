from django.shortcuts import render,render_to_response
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def userInfo(request):
    if request.method=='POST':
        id=int(request.POST.get('id'))


def default(request):
    return render_to_response('userInfo.html')
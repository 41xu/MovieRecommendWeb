from django.shortcuts import render, render_to_response, HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import models


@csrf_exempt
def register(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        count = models.User.objects.filter(name=user_name)
        print(count)
        if len(count) == 0:
            user = models.User(name=str(user_name), password=str(password))
            user.save()
            return HttpResponse("<p> 注册成功！</p>")
        else:
            return render_to_response('register.html', {'error': "用户已存在，请重新输入或直接登录吧！"})

    return render_to_response('register.html')

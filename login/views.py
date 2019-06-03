from django.shortcuts import render,render_to_response,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from register.models import User


@csrf_exempt
def login(request):
    if request.method=='POST':
        name=request.POST.get('username')
        password=request.POST.get('password')
        count=User.objects.filter(name=name)
        if len(count)==0:
            return render_to_response('login.html',{'error':"用户不存在，请先注册！"})
        else:
            user=User.objects.get(name=name)
            if password==user.password:
                # return HttpResponseRedirect('/userInfo/%s'%name)
                return render_to_response('login.html',
                                          {'error':"虽然你登陆成功了但是还是返回了error，只因登陆成功的页面Xusy太懒了还没写！算了！反正你登陆成功了！"})
            else:
                return render_to_response('login.html',{'error':"密码错误，这真的是你的帐号吗？？？请重新输入！！！"})
    return render_to_response('login.html')

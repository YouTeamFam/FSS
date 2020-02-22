from django.shortcuts import render, redirect
from django.urls import reverse
from mainapp.models import TSup, TPtAdmin, TServ, TAdBm
from tools.md5_ import hash_encode


def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    elif request.method=="POST":
        error = None
        username = request.POST.get('username')
        password = request.POST.get('password')
        password = hash_encode(password)
        sup_users = TSup.objects.filter(name=username,pwd=password)#先查询超级管理员
        if sup_users.exists():#如果查到了
            user=sup_users.first()
        else:
            pt_users = TPtAdmin.objects.filter(name=username,pwd=password)#查询普通管理员
            if pt_users.exists():#如果查到了
                user=pt_users.first()
            else:
                kf_users = TServ.objects.filter(name=username,pwd=username)#查询客服
                if kf_users.exists():
                    user=kf_users.first()
                    user.login_state=1
                    user.save()
                else:
                    ad_users = TAdBm.objects.filter(name=username,pwd=password)#查询广告商
                    if ad_users.exists():
                        user=ad_users.first()
                    else:
                        error = '账号密码有误，请重新输入'
                        return render(request, 'login.html', locals())
        request.session['name'] = user.name
        request.session['type'] = user.type
        return redirect("/")



def index(request):#登录成功后的页面
    return render(request, 'dashboard.html')


def logout(request):
    request.session.flush()
    return redirect('/login/')


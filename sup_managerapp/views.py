from django.core.paginator import Paginator
from django.shortcuts import render,redirect,reverse
import json
from tools.md5_ import hash_encode
import datetime
# Create your views here.
from sup_managerapp.models import *
from django.views import View
def sys_role_manage(request):
    pass


#内部角色管理【超级管理员，普通管理员，客服，广告商】
def role(request):
    action = request.GET.get('action', '')
    if action == 'del':
        T_Sys_Role.objects.get(pk=request.GET.get('role_id')).delete()

    roles = T_Sys_Role.objects.all()
    return render(request, 'role/list.html', locals())


class EditRoleView(View):
    def get(self, request):
        role_id = request.GET.get('role_id', '')
        if role_id:
            role = T_Sys_Role.objects.get(pk=role_id)
        return render(request, 'role/edit.html', locals())

    def post(self, request):
        """
        内部角色页面
        数据库先写入   再给后台写入
        可在后台修改已有的
        """
        from .forms import RoleForm
        role_id = request.POST.get('id', '')
        role_name = request.POST.get('name', '')
        role_type = request.POST.get('type', '')
        if role_id:
            form = RoleForm(request.POST, instance=T_Sys_Role.objects.get(pk=role_id))
            """
            有id说明是修改
            """
            if role_type == "超级管理员":
                role = TSup.objects.filter(type='超级管理员').first()
                role.name = role_name
                role.save()
            elif role_type == "普通管理员":
                role = TPtAdmin.objects.filter(type='普通管理员').first()
                role.name = role_name
                role.save()
            elif role_type == "客服":
                role = TServ.objects.filter(type='客服').first()
                role.name = role_name
                role.save()
            else:
                role = TAdBm.objects.filter(ad_bm_id=role_id).first()
                role.name = role_name
                role.save()
        else:
            form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sys_role_manage/')

        errors = json.loads(form.errors.as_json())
        return render(request, 'role/edit.html', locals())




#普通用户管理【便于搜索 查看 拉黑 删除】
def pt_user(request):
    action = request.GET.get('action', '')
    if action == 'del':
        TUser.objects.get(user_id=request.GET.get('role_id')).delete()
    pagenumber = request.GET.get("pagenumber", 1)
    userss = TUser.objects.all()
    paginator = Paginator(userss, 5)  # 每页最多显示3条记录
    users = paginator.page(pagenumber)
    return render(request, 'pt_user_role/list.html', locals())

class Edit_ptuser_View(View):
    def get(self, request):
        role_id = request.GET.get('role_id', '')
        if role_id:
            role = TUser.objects.get(user_id=role_id)
        return render(request, 'pt_user_role/edit.html', locals())

    def post(self, request):
        """
        普通用户页面
        分页器展示给后台
        可在后台修改已有的
        """
        from .forms import PtUserForm
        role_id = request.POST.get('id', '')
        if role_id:
            form = PtUserForm(request.POST, instance=TUser.objects.get(user_id=role_id))
            if form.is_valid():
                print("*" * 30)
                form.save()
                return redirect('/pt_user_manage/')

        else:
            name = request.POST.get("u_name")
            password = request.POST.get("u_pwd")
            sex = request.POST.get("sex")
            phone = request.POST.get("phone")
            # time1 = datetime.datetime.now()
            # time = str(time1)[:-7]
            """
            还没写推荐码  确定推荐吗后添加字段  并在前台展示推荐码添加字段
            """
            TUser.objects.create(u_name=name,u_pwd=password,sex=sex,phone=phone,status=0,balance=0)
            return redirect('/pt_user_manage/')

        errors = json.loads(form.errors.as_json())
        return render(request, 'pt_user_role/edit.html', locals())

#经纪人用户管理【便于搜索 查看 拉黑 删除】
def broker(request):
    action = request.GET.get('action', '')
    if action == 'del':

        #不用知道是不是外键原因  删除不了  会报错
        TBroker.objects.get(broker_id=request.GET.get('role_id')).delete()
    pagenumber = request.GET.get("pagenumber", 1)
    brokerss = TBroker.objects.all()
    paginator = Paginator(brokerss, 5)  # 每页最多显示3条记录
    brokers = paginator.page(pagenumber)
    return render(request, 'broker_manage/list.html', locals())

class Edit_broker_View(View):
    def get(self, request):
        role_id = request.GET.get('role_id', '')
        if role_id:
            role = TBroker.objects.get(broker_id=role_id)
            comname = TCompany.objects.filter(company_id=role.company_id).first()
            cname = comname.c_name
        commons = TCompany.objects.all()
        return render(request, 'broker_manage/edit.html', locals())

    def post(self, request):
        """
        普通用户页面
        分页器展示给后台
        可在后台修改已有的
        """
        role_id = request.POST.get('id', '')
        if role_id:
            jjr = TBroker.objects.get(broker_id=role_id)
            name = request.POST.get("b_name")
            uname = request.POST.get("b_uname")
            password = request.POST.get("b_pwd")
            sex = request.POST.get("sex")
            phone = request.POST.get("phone")
            common_id = request.POST.get("common_name")
            company = TCompany.objects.filter(company_id=common_id).first()
            jjr.b_name=name
            jjr.b_uname=uname
            jjr.b_pwd=password
            jjr.sex=sex
            jjr.phone=phone
            jjr.status=0
            jjr.clinch_num=0
            jjr.sou_num=0
            jjr.years=0
            jjr.company=company
            jjr.save()
            print("修改成功")
            return redirect('/broker_manage/')
        else:
            name = request.POST.get("b_name")
            uname = request.POST.get("b_uname")
            password = request.POST.get("b_pwd")
            sex = request.POST.get("sex")
            phone = request.POST.get("phone")
            common_id = request.POST.get("common_name")
            """
            先查出所属公司的id
            """
            company = TCompany.objects.filter(company_id=common_id).first()
            TBroker.objects.create(b_name=name,b_uname=uname,b_pwd=password,sex=sex,phone=phone,status=0,clinch_num=0,sou_num=0,years=0,company=company)
            return redirect('/broker_manage/')



'''房东个人信息'''
def fangdong(request):
    action = request.GET.get('action', '')
    if action == 'del':
        TLandlord.objects.get(pk=request.GET.get('fangdong_ld_id')).delete()#删除操作
    pagenumber = request.GET.get("pagenumber", 1)
    allfangs = TLandlord.objects.all()
    paginator = Paginator(allfangs,5)
    fangdongs = paginator.page(pagenumber)
    return render(request, 'fangdong/list.html', locals())

class FangDongView(View):
    def get(self, request):
        fangdong_ld_id = request.GET.get('fangdong_ld_id', '')
        if fangdong_ld_id:
            fangdong = TLandlord.objects.get(pk=fangdong_ld_id)
        return render(request, 'fangdong/edit.html', locals())
    def post(self,request):
        l_pwd = request.POST.get('l_pwd', '')
        l_pwd = hash_encode(l_pwd)
        from sup_managerapp.forms import FangDongForm
        ld_id=request.POST.get('fangdong_id', '')#用来判断是编辑还是创建
        if ld_id:
            form = FangDongForm(request.POST, instance=TLandlord.objects.get(pk=ld_id))
        else:
            form = FangDongForm(request.POST)
        if form.is_valid():
            form.save()
            fd = TLandlord.objects.get(l_uname=request.POST.get('l_uname'))#根据账号查，账号唯一
            fd.l_pwd=l_pwd
            fd.save()
            return redirect('/fd_manage/')
        errors = json.loads(form.errors.as_json())
        return render(request, 'fangdong/edit.html', locals())

'''二手房信息'''
def ershou(request):
    action = request.GET.get('action', '')
    if action == 'del':
        TSecondSource.objects.get(pk=request.GET.get('fang_source2_id')).delete()#删除操作
    pagenumber = request.GET.get("pagenumber", 1)
    ershous = TSecondSource.objects.all()
    paginator = Paginator(ershous,5)
    fangs = paginator.page(pagenumber)
    return render(request, 'ershou/list.html', locals())


class ErShouView(View):
    def get(self, request):
        fang_source2_id = request.GET.get('fang_source2_id', '')
        if fang_source2_id:
            fang = TSecondSource.objects.get(pk=fang_source2_id)
        return render(request, 'ershou/edit.html', locals())

    def post(self,request):
        from sup_managerapp.forms import ErShouForm
        fang_source2_id=request.POST.get('fang_id', '')
        form = ErShouForm(request.POST, instance=TSecondSource.objects.get(pk=fang_source2_id))
        if form.is_valid():
            form.save()
            return redirect('/ershou_manage/')
        errors = json.loads(form.errors.as_json())
        return render(request, 'ershou/edit.html', locals())


'''新房信息管理'''
def xinfang(request):
    action = request.GET.get('action', '')
    if action == 'del':
        TSource.objects.get(pk=request.GET.get('xinfang_source_id')).delete()#删除操作
    pagenumber = request.GET.get("pagenumber", 1)
    xins = TSource.objects.all()
    paginator = Paginator(xins,5)
    xinfangs = paginator.page(pagenumber)
    return render(request, 'xinfang/list.html', locals())


class XinFangView(View):
    def get(self, request):
        xinfang_source_id = request.GET.get('xinfang_source_id', '')
        if xinfang_source_id:
            xinfang = TSource.objects.get(pk=xinfang_source_id)
        return render(request, 'xinfang/edit.html', locals())

    def post(self,request):
        from sup_managerapp.forms import XinFangForm
        xinfang_source_id=request.POST.get('xinfang_id', '')
        form = XinFangForm(request.POST, instance=TSource.objects.get(pk=xinfang_source_id))
        if form.is_valid():
            form.save()
            return redirect('/xinfang_manage/')
        errors = json.loads(form.errors.as_json())
        return render(request, 'xinfang/edit.html', locals())


#消息推送  --user
def tuiuser(request):
    objs = TMessage.objects.all()
    action = request.GET.get('action', '')
    if action == 'del':
        TMessage.objects.get(pk=request.GET.get('id_')).delete()

    return render(request, 'message/list.html', locals())


class EditMessageUserView(View):
    def get(self, request):
        id_ = request.GET.get('id_', '')
        if id_:
            obj = TMessage.objects.get(pk=id_)

        return render(request, 'message/edit.html', locals())

    def post(self, request):
        from .forms import MessageForm
        id_ = request.POST.get('id_', '')
        if id_:
            form = MessageForm(request.POST, instance=TMessage.objects.get(pk=id_))
        else:
            form = MessageForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/tui_pt_user/')

        errors = json.loads(form.errors.as_json())
        return render(request, 'message/edit.html', locals())


#消息推送 ----fd
def tuifd(request):
    objs = TMessage.objects.all()
    action = request.GET.get('action', '')
    if action == 'del':
        TMessage.objects.get(pk=request.GET.get('id_')).delete()

    return render(request, 'message/list_fd.html', locals())


class EditMessageFdView(View):
    def get(self, request):
        id_ = request.GET.get('id_', '')
        if id_:
            obj = TMessage.objects.get(pk=id_)

        return render(request, 'message/edit_fd.html', locals())

    def post(self, request):
        from .forms import MessageForm
        id_ = request.POST.get('id_', '')
        if id_:
            form = MessageForm(request.POST, instance=TMessage.objects.get(pk=id_))
        else:
            form = MessageForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/tui_mes_fd/')

        errors = json.loads(form.errors.as_json())
        return render(request, 'message/edit_fd.html', locals())


#消息推送 ----jjr
def tuijjr(request):
    objs = TMessage.objects.all()
    action = request.GET.get('action', '')
    if action == 'del':
        TMessage.objects.get(pk=request.GET.get('id_')).delete()

    return render(request, 'message/list_jjr.html', locals())


class EditMessageJjrView(View):
    def get(self, request):
        id_ = request.GET.get('id_', '')
        if id_:
            obj = TMessage.objects.get(pk=id_)

        return render(request, 'message/edit_jjr.html', locals())

    def post(self, request):
        from .forms import MessageForm
        id_ = request.POST.get('id_', '')
        if id_:
            form = MessageForm(request.POST, instance=TMessage.objects.get(pk=id_))
        else:
            form = MessageForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/tui_mes_jjr/')

        errors = json.loads(form.errors.as_json())
        return render(request, 'message/edit_jjr.html', locals())


#选择要推送的用户  selectuser
def selectuser(request):
    m_id = request.GET.get('id_')
    pagenumber = request.GET.get("pagenumber", 1)
    userss = TUser.objects.all()
    paginator = Paginator(userss, 5)  # 每页最多显示3条记录
    users = paginator.page(pagenumber)

    return render(request, 'message/select_user.html', locals())

def fasong_user(request):
    m_id = request.GET.get('m_id')
    ids = request.GET.get('ids')
    ids = ids.split(",")
    text = TMessage.objects.get(message_id=m_id)
    for id_ in ids:
        id_ = int(id_)
        #我给模型多加了个  mes_text  字段 明天用王凯models的时候吧mes_text字段加上就行  数据库mes_text字段已建好
        user = TUser.objects.get(user_id=id_)
        user.mes_text = text.content
        user.mes_title = text.title
        user.save()
    return redirect("/tui_pt_user/")



def selectfd(request):
    m_id = request.GET.get('id_')
    pagenumber = request.GET.get("pagenumber", 1)
    userss = TLandlord.objects.all()
    paginator = Paginator(userss, 5)  # 每页最多显示3条记录
    users = paginator.page(pagenumber)

    return render(request, 'message/select_fd.html', locals())


def fasong_fd(request):
    m_id = request.GET.get('m_id')
    ids = request.GET.get('ids')
    ids = ids.split(",")
    text = TMessage.objects.get(message_id=m_id)
    for id_ in ids:
        id_ = int(id_)
        #扎块只能一个一个选择推送   + - 号没改push
        #我给模型多加了个  mes_text  字段 明天用王凯models的时候吧mes_text字段加上就行  数据库mes_text字段已建好
        user = TLandlord.objects.get(ld_id=id_)
        user.mes_text = text.content
        user.mes_title = text.title
        user.save()
    return redirect("/tui_mes_fd/")



def selectjjr(request):
    m_id = request.GET.get('id_')
    pagenumber = request.GET.get("pagenumber", 1)
    userss = TBroker.objects.all()
    paginator = Paginator(userss, 5)  # 每页最多显示3条记录
    users = paginator.page(pagenumber)
    return render(request, 'message/select_jjr.html', locals())


def fasong_jjr(request):
    m_id = request.GET.get('m_id')
    ids = request.GET.get('ids')
    ids = ids.split(",")
    text = TMessage.objects.get(message_id=m_id)
    for id_ in ids:
        id_ = int(id_)
        #我给模型多加了个  mes_text  字段 明天用王凯models的时候吧mes_text字段加上就行  数据库mes_text字段已建好
        user = TBroker.objects.get(broker_id=id_)
        user.mes_text = text.content
        user.mes_title = text.title
        user.save()
    return redirect("/tui_mes_jjr/")







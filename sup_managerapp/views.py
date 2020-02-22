from django.shortcuts import render,redirect,reverse
import json
# Create your views here.
from sup_managerapp.models import *
from django.views import View
def sys_role_manage(request):
    pass

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
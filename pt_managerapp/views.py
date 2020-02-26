from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View


from pt_managerapp.models import *
from tools.md5_ import hash_encode

'''
    审核广告
'''
class AdMessageView(View):
    def get(self, request):
        # pwd = hash_encode('luyao123')
        # TAdBm.objects.create(name='luyao',pwd=pwd,type='广告商')
        #         # TAdPos.objects.create(c_pos='右下角')
        # new_ad  = TAd.objects.create(ad_pos_id=1,ad_bm_id=1,
        #                              title='中医药为抗击疫情贡献力量',
        #                              img_url='/pt_managerapp/ad/ad1.jpg',
        #                              ad_url='http://jrb.xinjiang.gov.cn/xwdt/2020/11224.htm',audit_state=0)
        # pwd = hash_encode('lx1234') 广告商2
        # new_ad  = TAd.objects.create(ad_pos_id=3,ad_bm_id=2,
        #                              title='西安市十大旅游景点',
        #                              img_url='/pt_managerapp/ad/ad2.jpg',
        #                              ad_url='http://www.bytravel.cn/view/top10/index213.html',audit_state=0)
        new_ad = TAd.objects.filter(audit_state=0).all()
        if new_ad:
            new_ad = new_ad
        else:
            new_ad = None
        return render(request, 'pt_message/ad/guanggao_audit.html', locals())


class AdAuditMessage(View):
    def get(self, request):
        action = request.GET.get('action', '')
        if action:
            tad = TAd.objects.get(pk=request.GET.get('id_'))
            if action == 'yes':
                tad.audit_state = 1
            elif action == 'no':
                tad.audit_state = 2
                tad.note=request.GET.get('note', '')  #不通过理由
            tad.save()

        new_ad = TAd.objects.filter(audit_state=0).all()
        return render(request,'pt_message/ad/guanggao_audit.html',locals())


#删除不通过的广告 【可选】
def ad_message(request):
    action = request.GET.get('action', '')
    if action == 'del':
        TAd.objects.get(pk=request.GET.get('id_')).delete()

    nuw_guangGao = TAd.objects.filter(Q(audit_state=1) | Q(audit_state=2)).all()
    return render(request, 'pt_message/ad/ad_list.html',locals())



def ad_check_record(request):
    t_ad = request.GET.get('id_', '')
    # print(t_ad)
    status = request.GET.get('status','')
    status = int(status)
    name = request.session['name']  #获取当前用户
    user = TPtAdmin.objects.get(name=name)
    if t_ad and status:
        #查询记录表是否有这条记录
        ad_check = TAdCheckRecord.objects.filter(ad_id=t_ad)
        if ad_check.exists(): #不为空
            ad_check = ad_check.first()
            if ad_check.ad_id != t_ad and ad_check.is_pass != status:
                if status == 1:
                    TAdCheckRecord.objects.create(pt_id=user.pt_id, ad_id=t_ad, is_pass=status)
                elif status == 2:
                    TAdCheckRecord.objects.create(pt_id=user.pt_id, ad_id=t_ad, is_pass=status)
        else:
            if status == 1:
                TAdCheckRecord.objects.create(pt_id=user.pt_id, ad_id=t_ad, is_pass=status)
            elif status == 2:
                TAdCheckRecord.objects.create(pt_id=user.pt_id, ad_id=t_ad, is_pass=status)
        new_ad_check = TAdCheckRecord.objects.filter(ad_id=t_ad).all()
        return render(request, 'pt_message/ad/ad_checkrecord_one.html', locals())
    else:
        return redirect('/ad_list/')


def ad_all(request):
    ad_all = TAdCheckRecord.objects.all()
    if ad_all.exists():
        ad_all = ad_all.all()
    else:
        ad_all = None
    return render(request, 'pt_message/ad/ad_checkrecord_list.html', locals())


'''
    审核房源(新房和二手房)
'''

def x_fang_source(request):
    new_x_source  = TSource.objects.filter(ch_state=0).all()

    if  new_x_source :
        x_source = new_x_source

    else:
        x_source = None

    return render(request, 'pt_message/fy/xf_source_check.html', locals())

def j_fang_source(request):
    new_j_source =  TSecondSource.objects.filter(ch_state=0).all()
    if new_j_source:
        j_source = new_j_source
    else:
        j_source = None
    return render(request, 'pt_message/fy/jf_source_check.html', locals())


#根据前端审核情况判断审核状态
def xf_check(request):
    action = request.GET.get('action', '')
    if action:
        x_source = TSource.objects.get(pk=request.GET.get('id_'))

        if action == 'yes':
            x_source.ch_state = 1
        elif action == 'no':
            x_source.ch_state = 2
            x_source.note=request.GET.get('note', '')  #不通过理由
        x_source.save()

    x_source= TSource.objects.filter(ch_state=0).all()
    return render(request,'pt_message/fy/xf_source_check.html',locals())

def jf_check(request):
    action = request.GET.get('action', '')
    if action:
        j_source = TSecondSource.objects.get(pk=request.GET.get('id_'))

        if action == 'yes':
            j_source.ch_state = 1
        elif action == 'no':
            j_source.ch_state = 2
            j_source.note = request.GET.get('note', '')  # 不通过理由
        j_source.save()

    j_source = TSecondSource.objects.filter(ch_state=0).all()
    return render(request, 'pt_message/fy/jf_source_check.html', locals())


#删除不通过的房源 【可选】
def x_check_message(request):
    action = request.GET.get('action', '')
    if action == 'del':
        TSource.objects.get(pk=request.GET.get('id_')).delete()

    x_source = TSource.objects.filter(Q(ch_state=1) | Q(ch_state=2)).all()
    if x_source:
        x_source = x_source
    else:
        x_source = None
    return render(request, 'pt_message/fy/xfy_check.html', locals())

def j_check_message(request):
    action = request.GET.get('action', '')
    if action == 'del':
        TSecondSource.objects.get(pk=request.GET.get('id_')).delete()

    j_source = TSecondSource.objects.filter(Q(ch_state=1) | Q(ch_state=2)).all()
    if j_source:
        j_source = j_source
    else:
        j_source = None
    return render(request, 'pt_message/fy/jfy_check.html', locals())


#将前端审核信息存储到房源记录表中
def xf_check_record(request):
    id = request.GET.get('id_', '')
    status = request.GET.get('status','')
    name = request.session['name']  #获取当前用户
    user = TPtAdmin.objects.get(name=name)
    if id and status:
        #查询记录表是否有这条记录
        x_check = TCheckHousetie.objects.filter(source_id=id)
        if x_check.exists(): #不为空
            x_check = x_check.first()
            if x_check.source_id != id and x_check.is_pass != status:
                if status == 1:
                    TCheckHousetie.objects.create(pt_id=user.pt_id, source_id=id, is_pass=status)
                elif status == 2:
                    TCheckHousetie.objects.create(pt_id=user.pt_id, source_id=id, is_pass=status)
        else:
            if status == 1:
                TCheckHousetie.objects.create(pt_id=user.pt_id, source_id=id, is_pass=status)
            elif status == 2:
                TCheckHousetie.objects.create(pt_id=user.pt_id, source_id=id, is_pass=status)
        new_xf_check = TCheckHousetie.objects.filter(source_id=id).all()
        return render(request, 'pt_message/fy/xf_checkrecord_one.html/',locals())
    else:
        return redirect('/x_message/')

#二手房
def jf_check_record(request):
    id = request.GET.get('id_', '')
    status = request.GET.get('status', '')
    name = request.session['name']  #获取当前用户
    user = TPtAdmin.objects.get(name=name)
    if id and status:
        #查询记录表是否有这条记录
        j_check = TCheckHousetie.objects.filter(source2_id=id)
        if j_check.exists(): #不为空
            j_check = j_check.first()
            if j_check.source2_id != id and j_check.is_pass != status:
                if status == 1:
                    TCheckHousetie.objects.create(pt_id=user.pt_id, source2_id=id, is_pass=status)
                elif status == 2:
                    TCheckHousetie.objects.create(pt_id=user.pt_id, source2_id=id, is_pass=status)
        else:
            if status == 1:
                TCheckHousetie.objects.create(pt_id=user.pt_id, source2_id=id, is_pass=status)
            elif status == 2:
                TCheckHousetie.objects.create(pt_id=user.pt_id, source2_id=id, is_pass=status)
        new_jf_check = TCheckHousetie.objects.filter(source2_id=id).all()
        return render(request, 'pt_message/fy/jf_checkrecord_one.html/', locals())
    else:
        return redirect('/j_message/')


#全部审核记录表
def fy_check_list(request):
    fy_list = j_check = TCheckHousetie.objects.all()
    if fy_list.exists():
        fy_list = fy_list.all()
    else:
        fy_list = None
    return render(request, 'pt_message/fy/fy_checkrecord_list.html/', locals())


'''
    发帖信息【可以查看 删除】
'''
def post_message(request):
    user_post = TUserPost.objects.all()
    action = request.GET.get('action', '')
    if action == 'del':
        TUserPost.objects.get(pk=request.GET.get('id_')).delete()

    user_post = TUserPost.objects.all()
    if user_post.exists():
        user_post = user_post.all()
    else:
        user_post = None
    return render(request,'pt_message/ft/ft_list.html',locals())


def check_ft_details(request):
    id = request.GET.get('id_', '')
    ft_list = TUserPost.objects.get(pk=id)
    return render(request,'pt_message/ft/check_ft_details.html',locals())


'''
    举报投诉
'''
def complaint_view(request):
    complaint_list = TReportComplaints.objects.filter(is_pass=0)
    if complaint_list.exists():
        complaint_all = complaint_list.all()
    else:
        complaint_all = None
    return render(request,'pt_message/ts/ts_message.html',locals())


def dispose_complaint_view(request):
    action = request.GET.get('action', '')
    if action:
        complaints = TReportComplaints.objects.get(pk=request.GET.get('id_'))
        if action == 'yes':
            complaints.is_pass = 1
        elif action == 'no':
            complaints.is_pass = 2
        complaints.note = request.GET.get('note', '')  #处理内容和不处理理由
        complaints.save()

    complaint_all= TReportComplaints.objects.filter(is_pass=0).all()
    return render(request, 'pt_message/ts/ts_message.html', locals())


def select_all_complaint(request):
    complaint_list = TReportComplaints.objects.filter(Q(is_pass=1) | Q(is_pass=2))
    if complaint_list.exists():
        complaint_all = complaint_list.all()
    else:
        complaint_all = None
    return render(request,'pt_message/ts/complaint_list.html',locals())


def detail_content_view(request):
    id = request.GET.get('id_', '')
    complaint = TReportComplaints.objects.get(pk=id)
    return render(request,'pt_message/ts/detail.html',locals())
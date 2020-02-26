from django.core.paginator import Paginator
from django.shortcuts import render,redirect
import json
# Create your views here.
from mainapp.models import TAd, TAdBm, TAdPos

from django.views import View


'''广告信息'''
def ad(request):
    action = request.GET.get('action', '')
    pagenumber = request.GET.get("pagenumber", 1)
    ren = TAdBm.objects.filter(name=request.session['name']).first()
    allads = TAd.objects.filter(ad_bm=ren)
    paginator = Paginator(allads,5)
    ads = paginator.page(pagenumber)
    return render(request, 'ad/list.html', locals())


class AdView(View):
    def get(self,request):
        ad_ad_id = request.GET.get('ad_ad_id', '')
        ren = TAdBm.objects.filter(name=request.session['name']).first()
        if ad_ad_id:
            ad = TAd.objects.get(pk=ad_ad_id)
        return render(request, 'ad/edit.html', locals())
    def post(self,request):
        ad_id = request.POST.get('ad_id', '')  # 用来判断是编辑还是创建
        from ad_managerapp.forms import AdForm
        if ad_id:
            form = AdForm(request.POST,request.FILES, instance=TAd.objects.get(pk=ad_id))
        else:
            form = AdForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            form.save()

            return redirect('/ad_manage/')
        errors = json.loads(form.errors.as_json())
        return render(request, 'ad/edit.html', locals())


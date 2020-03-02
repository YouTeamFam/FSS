# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone

class TAdPos(models.Model):
    ad_pos_id = models.AutoField(primary_key=True)
    c_pos = models.CharField(max_length=30,null=True)

    class Meta:
        db_table = 't_ad_pos'


class TAdBm(models.Model):
    ad_bm_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    pwd = models.CharField(max_length=255)
    ad_num = models.IntegerField(default=0)
    set_time = models.DateTimeField(default =timezone.now)
    val_ad_num = models.IntegerField(default=0)
    type = models.CharField(max_length=30)

    class Meta:
        db_table = 't_ad_bm'




class TAd(models.Model):
    ad_id = models.AutoField(primary_key=True)  # 广告编号
    ad_pos = models.ForeignKey(TAdPos, models.CASCADE,default=1)  # 广告位置id
    ad_bm = models.ForeignKey(TAdBm, models.CASCADE)  # 关联广告商
    title = models.CharField(max_length=30)  # 标题
    img_url = models.ImageField(upload_to='ad')  # 图片地址,这里对应的是上传图片对应的路径
    ad_url = models.CharField(max_length=255)  # 外部连接
    fabu_time = models.DateTimeField(default=timezone.now)  # 发布时间
    val = models.IntegerField(default=20)  # 有效时间
    audit_state = models.IntegerField(default=0)  # 审核状态
    note = models.TextField(default='略')  # 没通过理由

    class Meta:
        ordering=['ad_id']
        db_table = 't_ad'


class TPtAdmin(models.Model):
    pt_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    pwd = models.CharField(max_length=255)
    type = models.CharField(max_length=100)

    class Meta:
        db_table = 't_pt_admin'


class TAdCheckRecord(models.Model):
    ad_check_id = models.AutoField(primary_key=True)
    pt = models.ForeignKey(TPtAdmin, models.CASCADE)
    ad = models.ForeignKey(TAd, models.CASCADE)
    is_pass = models.IntegerField()

    class Meta:
        db_table = 't_ad_check_record'


class TAdExpireRenew(models.Model):
    ad_renew_id = models.AutoField(primary_key=True)
    ad = models.ForeignKey(TAd, models.CASCADE)
    is_renew = models.IntegerField(null=True)

    class Meta:
        db_table = 't_ad_expire_renew'


class TSup(models.Model):
    sup_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    pwd = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    class Meta:
        db_table = 't_sup'


class TAdNews(models.Model):
    ad_news_id = models.AutoField(primary_key=True)
    ad = models.ForeignKey(TAd, models.CASCADE,  null=True)
    sup = models.ForeignKey(TSup, models.CASCADE, null=True)
    news_title = models.CharField(max_length=50, null=True)
    content = models.CharField(max_length=255, null=True)
    date = models.DateTimeField(default=timezone.now)
    class Meta:
        db_table = 't_ad_news'


class TCompany(models.Model):
    company_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = 't_company'


class TBroker(models.Model):
    broker_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(TCompany, models.CASCADE)
    b_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    b_uname = models.CharField(max_length=30)
    b_pwd = models.CharField(max_length=255)
    avatar_path = models.CharField(db_column='Avatar_path', max_length=255,null=True)  # Field name made lowercase.
    regi_date = models.DateTimeField(default=timezone.now)
    status = models.IntegerField()
    clinch_num = models.IntegerField()
    sou_num = models.IntegerField()
    years = models.IntegerField()
    mes_text = models.TextField(null=True)
    mes_title = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 't_broker'

class TSource(models.Model):
    source_id = models.AutoField(primary_key=True)
    broker = models.ForeignKey(TBroker, models.CASCADE)
    title = models.CharField(max_length=30)
    img_url = models.CharField(max_length=255)
    pub_date = models.DateTimeField(default=timezone.now)
    nearby = models.CharField(max_length=255, null=True)
    region = models.CharField(max_length=30)
    hu_type = models.CharField(max_length=30, null=True)
    price_s = models.FloatField(null=True)
    comm_name = models.CharField(max_length=30,null=True)
    area = models.FloatField(null=True)
    sum_price = models.FloatField(null=True)
    face = models.CharField(max_length=30,null=True)
    details = models.CharField(max_length=255,null=True)
    floors = models.IntegerField(null=True)
    k_time = models.DateTimeField(null=True)
    ch_state = models.IntegerField(default=0)
    note = models.TextField(default='略')  # 没通过理由

    class Meta:
        ordering = ['source_id']
        db_table = 't_source'


class TLandlord(models.Model):
    ld_id = models.AutoField(primary_key=True)
    l_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    l_uname = models.CharField(max_length=30)
    l_pwd = models.CharField(max_length=255)
    avatar_path = models.CharField(db_column='Avatar_path', max_length=255,default='')  # Field name made lowercase.
    regi_date = models.DateTimeField(default=timezone.now)  # 创建时间，并且可以修改
    last_date = models.DateTimeField(auto_now=True)  # 修改时间
    status = models.IntegerField(default=1)
    sou_num = models.IntegerField(default=0)
    mes_text = models.TextField(null=True)
    mes_title = models.CharField(max_length=50, null=True)

    class Meta:
        ordering = ['regi_date']
        db_table = 't_landlord'


class TSecondSource(models.Model):
    source2_id = models.AutoField(primary_key=True)
    ld = models.ForeignKey(TLandlord, models.CASCADE,null=True)
    broker = models.ForeignKey(TBroker, models.CASCADE,null=True)
    title = models.CharField(max_length=50, null=True)
    img_url = models.CharField(max_length=255,null=True)
    pub_date = models.DateTimeField(default=timezone.now)
    nearby = models.CharField(max_length=50,null=True)
    region = models.CharField(max_length=50, null=True)
    hu_type = models.CharField(max_length=50, null=True)
    price_s = models.IntegerField(null=True)
    comm_name = models.CharField(max_length=30, null=True)
    area = models.FloatField(null=True)
    sum_price = models.FloatField(null=True)
    dis_price = models.FloatField(null=True)
    sell_rent = models.CharField(max_length=30,  null=True)
    rent_money = models.FloatField(null=True)
    face = models.CharField(max_length=30, null=True)
    details = models.CharField(max_length=50,null=True)
    floors = models.IntegerField(null=True)
    ch_state = models.IntegerField(default=0)
    fav_num = models.IntegerField(null=True)
    comment_num = models.IntegerField(null=True)
    shared_num = models.IntegerField( null=True)
    note = models.TextField(default='略')  # 没通过理由

    class Meta:
        ordering = ['source2_id']
        db_table = 't_second_source'


class TCheckHousetie(models.Model):
    check_house_id = models.AutoField(primary_key=True)
    pt = models.ForeignKey(TPtAdmin, models.CASCADE,  null=True)
    source = models.ForeignKey(TSource, models.CASCADE, null=True)
    source2 = models.ForeignKey(TSecondSource, models.CASCADE,  null=True)
    is_pass = models.IntegerField()

    class Meta:
        db_table = 't_check_housetie'


class TCommunity(models.Model):
    comm_hpk_id = models.AutoField(primary_key=True)
    source = models.ForeignKey(TSource, models.CASCADE, null=True)

    class Meta:
        db_table = 't_community'


class TUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    sex = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    avatar_path = models.CharField(max_length=255,  null=True)  # Field name made lowercase.
    u_name = models.CharField(max_length=50)
    u_pwd = models.CharField(max_length=255)
    status = models.IntegerField()
    balance = models.FloatField()
    regi_date = models.DateTimeField(default=timezone.now)  # 创建时间，并且可以修改
    last_date = models.DateTimeField(auto_now=True)  # 修改时间
    times = models.IntegerField( null=True)
    code = models.CharField(max_length=20,null=True)
    code_num = models.IntegerField(null=True)
    mes_text = models.TextField(null=True)
    mes_title = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 't_user'


class TForwardNews(models.Model):
    message_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(TUser, models.CASCADE)
    sup = models.ForeignKey(TSup, models.CASCADE)
    mess_title = models.CharField(max_length=50)
    content = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 't_forward_news'




class TNewImgDetails(models.Model):
    new_id = models.AutoField(primary_key=True)
    source = models.ForeignKey(TSource, models.CASCADE)
    pic_url = models.CharField(max_length=255)
    title = models.CharField(max_length=100)
    width = models.FloatField(null=True)
    height = models.FloatField(null=True)

    class Meta:
        db_table = 't_new_img_details'


class TNewTransaction(models.Model):
    new_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(TUser, models.CASCADE)
    source = models.ForeignKey(TSource, models.CASCADE)
    deposit_amount = models.FloatField()
    deposit_date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 't_new_transaction'



class TRentalTransaction(models.Model):
    rental_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(TUser, models.CASCADE)
    source2 = models.ForeignKey(TSecondSource, models.CASCADE)
    deposit_amount = models.FloatField()
    deposit_date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 't_rental_transaction'


class TReportComplaints(models.Model):
    report_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(TUser, models.CASCADE)
    source = models.ForeignKey(TSource, models.CASCADE,null=True)
    source2 = models.ForeignKey(TSecondSource, models.CASCADE,null=True)
    pt = models.ForeignKey(TPtAdmin, models.CASCADE, null=True)
    content = models.TextField(null=True)
    phone = models.CharField(max_length=30, null=True)
    date = models.DateTimeField(default=timezone.now)
    is_pass = models.IntegerField()
    note = models.TextField(default='')   #处理结果

    class Meta:
        db_table = 't_report_complaints'


class TSecImgDetails(models.Model):
    second_id = models.AutoField(primary_key=True)
    source2 = models.ForeignKey(TSecondSource, models.CASCADE)
    pic_url = models.CharField(max_length=255)
    title = models.CharField(max_length=100)
    width = models.FloatField(null=True)
    height = models.FloatField(null=True)

    class Meta:
        db_table = 't_sec_img_details'


class TSecondGoodHouse(models.Model):
    source2_good_id = models.AutoField(primary_key=True)
    source2 = models.ForeignKey(TSecondSource, models.CASCADE, null=True)

    class Meta:
        db_table = 't_second_good_house'


class TSecondHandTransaction(models.Model):
    sec_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(TUser, models.CASCADE)
    source2 = models.ForeignKey(TSecondSource, models.CASCADE)
    deposit_amount = models.FloatField()
    deposit_date = models.DateTimeField(null=True)

    class Meta:
        db_table = 't_second_hand_transaction'


class TSelectRentalHouse(models.Model):
    select_good_id = models.AutoField(primary_key=True)
    source2 = models.ForeignKey(TSecondSource, models.CASCADE,null=True)

    class Meta:
        db_table = 't_select_rental_house'


class TServ(models.Model):
    serv_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,null=True)
    pwd = models.CharField(max_length=255,  null=True)
    ser_phone = models.CharField(max_length=50, null=True)
    login_state = models.IntegerField(default=0)
    type = models.CharField(max_length=30,default='客服')

    class Meta:
        db_table = 't_serv'


class TUserVip(models.Model):
    vip_id = models.AutoField(primary_key=True)
    vip_grade = models.IntegerField(db_column='VIP_grade',  null=True)  # Field name made lowercase.
    integral = models.IntegerField( null=True)

    class Meta:
        db_table = 't_user_VIP'


class TUserPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(TUser, models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    tie_pic = models.CharField(max_length=255)
    class Meta:
        db_table = 't_user_post'


class TUserComment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(TUser, models.CASCADE)
    source = models.ForeignKey(TSource, models.CASCADE, null=True)
    source2 = models.ForeignKey(TSecondSource, models.CASCADE, null=True)
    post = models.ForeignKey(TUserPost, models.CASCADE)
    content = models.TextField()
    comment_type = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 't_user_comment'


class TUserFavourity(models.Model):
    fav_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(TUser, models.CASCADE)
    source = models.ForeignKey(TSource, models.CASCADE, null=True)
    source2 = models.ForeignKey(TSecondSource, models.CASCADE,null=True)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 't_user_favourity'


class TUserHistory(models.Model):
    history_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(TUser, models.CASCADE)
    source = models.ForeignKey(TSource, models.CASCADE, null=True)
    source2 = models.ForeignKey(TSecondSource, models.CASCADE, null=True)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 't_user_history'


class TUserIntegral(models.Model):
    integ_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(TUser, models.CASCADE)
    integral = models.IntegerField(null=True)
    vip_grade = models.IntegerField(db_column='VIP_grade',null=True)  # Field name made lowercase.

    class Meta:
        db_table = 't_user_integral'


class TUserLd(models.Model):
    user_ld_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(TUser, models.CASCADE, null=True)
    ld = models.ForeignKey(TLandlord, models.CASCADE,null=True)
    content = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 't_user_ld'





class TUserRecharge(models.Model):
    recharge_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(TUser, models.CASCADE)
    recharge_type = models.CharField(max_length=50,  null=True)
    recharge_amount = models.FloatField()
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 't_user_recharge'


class TUserServ(models.Model):
    user_serv_id = models.AutoField(primary_key=True)
    serv = models.ForeignKey(TServ, models.CASCADE, null=True)
    user = models.ForeignKey(TUser, models.CASCADE, null=True)
    content = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 't_user_serv'


class TUserShare(models.Model):
    share_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(TUser, models.CASCADE)
    source = models.ForeignKey(TSource, models.CASCADE)
    source2 = models.ForeignKey(TSecondSource, models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 't_user_share'


class TWheelPic(models.Model):
    wheel_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=True)
    house_detail = models.CharField(max_length=255, null=True)
    img_path = models.ImageField(upload_to='wheel')

    class Meta:
        ordering = ['wheel_id']
        db_table = 't_wheel_pic'
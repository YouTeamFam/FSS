# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TAdPos(models.Model):
    ad_pos_id = models.AutoField(primary_key=True)
    c_pos = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_ad_pos'


class TAdBm(models.Model):
    ad_bm_id = models.AutoField(primary_key=True)
    a_uname = models.CharField(max_length=30)
    a_pwd = models.CharField(max_length=30)
    ad_num = models.IntegerField()
    set_time = models.DateTimeField()
    val_ad_num = models.IntegerField()
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_ad_bm'


class TAd(models.Model):
    ad_id = models.AutoField(primary_key=True)
    ad_pos = models.ForeignKey(TAdPos, models.DO_NOTHING)
    ad_bm = models.ForeignKey(TAdBm, models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=30)
    img_url = models.CharField(max_length=255)
    ad_url = models.CharField(max_length=255)
    fabu_time = models.DateTimeField(blank=True, null=True)
    val_time = models.DateTimeField(blank=True, null=True)
    is_ok = models.IntegerField(blank=True, null=True)
    audit_state = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_ad'


class TPtAdmin(models.Model):
    pt_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    type = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 't_pt_admin'


class TAdCheckRecord(models.Model):
    ad_check_id = models.AutoField(primary_key=True)
    pt = models.ForeignKey(TPtAdmin, models.DO_NOTHING)
    ad = models.ForeignKey(TAd, models.DO_NOTHING)
    is_pass = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_ad_check_record'


class TAdExpireRenew(models.Model):
    ad_renew_id = models.AutoField(primary_key=True)
    ad = models.ForeignKey(TAd, models.DO_NOTHING)
    is_renew = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_ad_expire_renew'


class TSup(models.Model):
    sup_id = models.AutoField(primary_key=True)
    sup_user = models.CharField(max_length=50)
    sup_pwd = models.CharField(max_length=50)
    type = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 't_sup'


class TAdNews(models.Model):
    ad_news_id = models.AutoField(primary_key=True)
    ad = models.ForeignKey(TAd, models.DO_NOTHING, blank=True, null=True)
    sup = models.ForeignKey(TSup, models.DO_NOTHING, blank=True, null=True)
    news_title = models.CharField(max_length=50, blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_ad_news'


class TCompany(models.Model):
    company_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_company'


class TBroker(models.Model):
    broker_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(TCompany, models.DO_NOTHING)
    b_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    b_uname = models.CharField(max_length=30)
    b_pwd = models.CharField(max_length=30)
    avatar_path = models.CharField(db_column='Avatar_path', max_length=255, blank=True, null=True)  # Field name made lowercase.
    regi_date = models.DateTimeField()
    status = models.IntegerField()
    clinch_num = models.IntegerField()
    sou_num = models.IntegerField()
    years = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_broker'


class TSource(models.Model):
    source_id = models.AutoField(primary_key=True)
    broker = models.ForeignKey(TBroker, models.DO_NOTHING)
    title = models.CharField(max_length=30)
    img_url = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    nearby = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=30)
    hu_type = models.CharField(max_length=30, blank=True, null=True)
    price_s = models.FloatField(blank=True, null=True)
    comm_name = models.CharField(max_length=30, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    sum_price = models.FloatField(blank=True, null=True)
    dis_price = models.FloatField(blank=True, null=True)
    face = models.CharField(max_length=30, blank=True, null=True)
    details = models.CharField(max_length=255, blank=True, null=True)
    floors = models.IntegerField(blank=True, null=True)
    k_time = models.DateTimeField(blank=True, null=True)
    ch_state = models.IntegerField(blank=True, null=True)
    is_check = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_source'


class TLandlord(models.Model):
    ld_id = models.AutoField(primary_key=True)
    l_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    l_uname = models.CharField(max_length=30)
    l_pwd = models.CharField(max_length=30)
    avatar_path = models.CharField(db_column='Avatar_path', max_length=255, blank=True, null=True)  # Field name made lowercase.
    regi_date = models.DateTimeField()
    last_date = models.DateTimeField()
    status = models.IntegerField()
    sou_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_landlord'


class TSecondSource(models.Model):
    source2_id = models.AutoField(primary_key=True)
    ld = models.ForeignKey(TLandlord, models.DO_NOTHING, blank=True, null=True)
    broker = models.ForeignKey(TBroker, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    img_url = models.CharField(max_length=255, blank=True, null=True)
    pub_date = models.DateTimeField(blank=True, null=True)
    nearby = models.CharField(max_length=50, blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    hu_type = models.CharField(max_length=50, blank=True, null=True)
    price_s = models.IntegerField(blank=True, null=True)
    comm_name = models.CharField(max_length=30, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    sum_price = models.FloatField(blank=True, null=True)
    dis_price = models.FloatField(blank=True, null=True)
    sell_rent = models.CharField(max_length=30, blank=True, null=True)
    rent_money = models.FloatField(blank=True, null=True)
    face = models.CharField(max_length=30, blank=True, null=True)
    details = models.CharField(max_length=50, blank=True, null=True)
    floors = models.IntegerField(blank=True, null=True)
    k_time = models.DateTimeField(blank=True, null=True)
    ch_state = models.IntegerField(blank=True, null=True)
    is_check = models.IntegerField(blank=True, null=True)
    fav_num = models.IntegerField(blank=True, null=True)
    comment_num = models.IntegerField(blank=True, null=True)
    shared_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_second_source'


class TCheckHousetie(models.Model):
    check_house_id = models.AutoField(primary_key=True)
    pt = models.ForeignKey(TPtAdmin, models.DO_NOTHING, blank=True, null=True)
    source = models.ForeignKey(TSource, models.DO_NOTHING, blank=True, null=True)
    source2 = models.ForeignKey(TSecondSource, models.DO_NOTHING, blank=True, null=True)
    is_pass = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_check_housetie'


class TCommunity(models.Model):
    comm_hpk_id = models.AutoField(primary_key=True)
    source = models.ForeignKey(TSource, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_community'


class TUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    sex = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    avatar_path = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    u_name = models.CharField(max_length=50)
    u_pwd = models.CharField(max_length=255)
    status = models.IntegerField()
    balance = models.FloatField()
    regi_date = models.DateTimeField()
    last_date = models.DateTimeField(blank=True, null=True)
    times = models.IntegerField(blank=True, null=True)
    code = models.CharField(blank=True, null=True)
    code_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user'


class TForwardNews(models.Model):
    message_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(TUser, models.DO_NOTHING)
    sup = models.ForeignKey(TSup, models.DO_NOTHING)
    mess_title = models.CharField(max_length=10)
    content = models.CharField(max_length=10)
    date = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_forward_news'





class TNewImgDetails(models.Model):
    new_id = models.AutoField(primary_key=True)
    source = models.ForeignKey(TSource, models.DO_NOTHING)
    pic_url = models.CharField(max_length=255)
    title = models.CharField(max_length=100)
    width = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_new_img_details'


class TNewTransaction(models.Model):
    new_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(TUser, models.DO_NOTHING)
    source = models.ForeignKey(TSource, models.DO_NOTHING)
    deposit_amount = models.FloatField()
    deposit_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_new_transaction'


class TRentalTransaction(models.Model):
    rental_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(TUser, models.DO_NOTHING)
    source2 = models.ForeignKey(TSecondSource, models.DO_NOTHING)
    deposit_amount = models.FloatField()
    deposit_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_rental_transaction'


class TReportComplaints(models.Model):
    report_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(TUser, models.DO_NOTHING)
    source = models.ForeignKey(TSource, models.DO_NOTHING, blank=True, null=True)
    source2 = models.ForeignKey(TSecondSource, models.DO_NOTHING, blank=True, null=True)
    pt = models.ForeignKey(TPtAdmin, models.DO_NOTHING, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    is_pass = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_report_complaints'


class TSecImgDetails(models.Model):
    second_id = models.AutoField(primary_key=True)
    source2 = models.ForeignKey(TSecondSource, models.DO_NOTHING)
    pic_url = models.CharField(max_length=255)
    title = models.CharField(max_length=100)
    width = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_sec_img_details'


class TSecondGoodHouse(models.Model):
    source2_good_id = models.AutoField(primary_key=True)
    source2 = models.ForeignKey(TSecondSource, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_second_good_house'


class TSecondHandTransaction(models.Model):
    sec_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(TUser, models.DO_NOTHING)
    source2 = models.ForeignKey(TSecondSource, models.DO_NOTHING)
    deposit_amount = models.FloatField()
    deposit_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_second_hand_transaction'


class TSelectRentalHouse(models.Model):
    sselect_good_id = models.AutoField(primary_key=True)
    source2 = models.ForeignKey(TSecondSource, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_select_rental_house'


class TServ(models.Model):
    serv_id = models.AutoField(primary_key=True)
    ser_user = models.CharField(max_length=50, blank=True, null=True)
    ser_pwd = models.CharField(max_length=50, blank=True, null=True)
    ser_phone = models.CharField(max_length=50, blank=True, null=True)
    login_state = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_serv'


class TUserVip(models.Model):
    vip_id = models.AutoField(primary_key=True)
    vip_grade = models.IntegerField(db_column='VIP_grade', blank=True, null=True)  # Field name made lowercase.
    integral = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user_VIP'


class TUserComment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(TUser, models.DO_NOTHING)
    source = models.ForeignKey(TSource, models.DO_NOTHING, blank=True, null=True)
    source2 = models.ForeignKey(TSecondSource, models.DO_NOTHING, blank=True, null=True)
    post = models.ForeignKey('TUserPost', models.DO_NOTHING)
    content = models.TextField()
    comment_type = models.CharField(max_length=100)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_user_comment'


class TUserFavourity(models.Model):
    fav_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(TUser, models.DO_NOTHING)
    source = models.ForeignKey(TSource, models.DO_NOTHING, blank=True, null=True)
    source2 = models.ForeignKey(TSecondSource, models.DO_NOTHING, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user_favourity'


class TUserHistory(models.Model):
    history_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(TUser, models.DO_NOTHING)
    source = models.ForeignKey(TSource, models.DO_NOTHING, blank=True, null=True)
    source2 = models.ForeignKey(TSecondSource, models.DO_NOTHING, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user_history'


class TUserIntegral(models.Model):
    integ_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(TUser, models.DO_NOTHING)
    integral = models.IntegerField(blank=True, null=True)
    vip_grade = models.IntegerField(db_column='VIP_grade', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_user_integral'


class TUserLd(models.Model):
    user_ld_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(TUser, models.DO_NOTHING, blank=True, null=True)
    ld = models.ForeignKey(TLandlord, models.DO_NOTHING, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user_ld'


class TUserPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(TUser, models.DO_NOTHING)
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_user_post'


class TUserRecharge(models.Model):
    recharge_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(TUser, models.DO_NOTHING)
    recharge_type = models.CharField(max_length=50, blank=True, null=True)
    recharge_amount = models.FloatField()
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user_recharge'


class TUserServ(models.Model):
    user_serv_id = models.AutoField(primary_key=True)
    serv = models.ForeignKey(TServ, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(TUser, models.DO_NOTHING, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user_serv'


class TUserShare(models.Model):
    share_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(TUser, models.DO_NOTHING)
    source = models.ForeignKey(TSource, models.DO_NOTHING)
    source2 = models.ForeignKey(TSecondSource, models.DO_NOTHING)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user_share'


class TWheelPic(models.Model):
    wheel_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    house_url = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_wheel_pic'
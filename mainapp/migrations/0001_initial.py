# Generated by Django 2.0.1 on 2020-02-20 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TAd',
            fields=[
                ('ad_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('img_url', models.CharField(max_length=255)),
                ('ad_url', models.CharField(max_length=255)),
                ('fabu_time', models.DateTimeField(null=True)),
                ('val_time', models.DateTimeField(null=True)),
                ('is_ok', models.IntegerField(null=True)),
                ('audit_state', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 't_ad',
            },
        ),
        migrations.CreateModel(
            name='TAdBm',
            fields=[
                ('ad_bm_id', models.AutoField(primary_key=True, serialize=False)),
                ('a_uname', models.CharField(max_length=30)),
                ('a_pwd', models.CharField(max_length=30)),
                ('ad_num', models.IntegerField()),
                ('set_time', models.DateTimeField()),
                ('val_ad_num', models.IntegerField()),
                ('type', models.IntegerField()),
            ],
            options={
                'db_table': 't_ad_bm',
            },
        ),
        migrations.CreateModel(
            name='TAdCheckRecord',
            fields=[
                ('ad_check_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_pass', models.IntegerField()),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.TAd')),
            ],
            options={
                'db_table': 't_ad_check_record',
            },
        ),
        migrations.CreateModel(
            name='TAdExpireRenew',
            fields=[
                ('ad_renew_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_renew', models.IntegerField(null=True)),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.TAd')),
            ],
            options={
                'db_table': 't_ad_expire_renew',
            },
        ),
        migrations.CreateModel(
            name='TAdNews',
            fields=[
                ('ad_news_id', models.AutoField(primary_key=True, serialize=False)),
                ('news_title', models.CharField(max_length=50, null=True)),
                ('content', models.CharField(max_length=255, null=True)),
                ('date', models.DateTimeField(null=True)),
                ('ad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.TAd')),
            ],
            options={
                'db_table': 't_ad_news',
            },
        ),
        migrations.CreateModel(
            name='TAdPos',
            fields=[
                ('ad_pos_id', models.AutoField(primary_key=True, serialize=False)),
                ('c_pos', models.CharField(max_length=30, null=True)),
            ],
            options={
                'db_table': 't_ad_pos',
            },
        ),
        migrations.CreateModel(
            name='TBroker',
            fields=[
                ('broker_id', models.AutoField(primary_key=True, serialize=False)),
                ('b_name', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('b_uname', models.CharField(max_length=30)),
                ('b_pwd', models.CharField(max_length=30)),
                ('avatar_path', models.CharField(db_column='Avatar_path', max_length=255, null=True)),
                ('regi_date', models.DateTimeField()),
                ('status', models.IntegerField()),
                ('clinch_num', models.IntegerField()),
                ('sou_num', models.IntegerField()),
                ('years', models.IntegerField()),
            ],
            options={
                'db_table': 't_broker',
            },
        ),
        migrations.CreateModel(
            name='TCheckHousetie',
            fields=[
                ('check_house_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_pass', models.IntegerField()),
            ],
            options={
                'db_table': 't_check_housetie',
            },
        ),
        migrations.CreateModel(
            name='TCommunity',
            fields=[
                ('comm_hpk_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 't_community',
            },
        ),
        migrations.CreateModel(
            name='TCompany',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=30, null=True)),
            ],
            options={
                'db_table': 't_company',
            },
        ),
        migrations.CreateModel(
            name='TForwardNews',
            fields=[
                ('message_id', models.AutoField(primary_key=True, serialize=False)),
                ('mess_title', models.CharField(max_length=10)),
                ('content', models.CharField(max_length=10)),
                ('date', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 't_forward_news',
            },
        ),
        migrations.CreateModel(
            name='TLandlord',
            fields=[
                ('ld_id', models.AutoField(primary_key=True, serialize=False)),
                ('l_name', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('l_uname', models.CharField(max_length=30)),
                ('l_pwd', models.CharField(max_length=30)),
                ('avatar_path', models.CharField(db_column='Avatar_path', max_length=255, null=True)),
                ('regi_date', models.DateTimeField()),
                ('last_date', models.DateTimeField()),
                ('status', models.IntegerField()),
                ('sou_num', models.IntegerField()),
            ],
            options={
                'db_table': 't_landlord',
            },
        ),
        migrations.CreateModel(
            name='TNewImgDetails',
            fields=[
                ('new_id', models.AutoField(primary_key=True, serialize=False)),
                ('pic_url', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=100)),
                ('width', models.FloatField(null=True)),
                ('height', models.FloatField(null=True)),
            ],
            options={
                'db_table': 't_new_img_details',
            },
        ),
        migrations.CreateModel(
            name='TNewTransaction',
            fields=[
                ('new_id', models.AutoField(primary_key=True, serialize=False)),
                ('deposit_amount', models.FloatField()),
                ('deposit_date', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 't_new_transaction',
            },
        ),
        migrations.CreateModel(
            name='TPtAdmin',
            fields=[
                ('pt_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 't_pt_admin',
            },
        ),
        migrations.CreateModel(
            name='TRentalTransaction',
            fields=[
                ('rental_id', models.AutoField(primary_key=True, serialize=False)),
                ('deposit_amount', models.FloatField()),
                ('deposit_date', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 't_rental_transaction',
            },
        ),
        migrations.CreateModel(
            name='TReportComplaints',
            fields=[
                ('report_id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(null=True)),
                ('phone', models.CharField(max_length=30, null=True)),
                ('date', models.DateTimeField(null=True)),
                ('is_pass', models.IntegerField()),
                ('pt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.TPtAdmin')),
            ],
            options={
                'db_table': 't_report_complaints',
            },
        ),
        migrations.CreateModel(
            name='TSecImgDetails',
            fields=[
                ('second_id', models.AutoField(primary_key=True, serialize=False)),
                ('pic_url', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=100)),
                ('width', models.FloatField(null=True)),
                ('height', models.FloatField(null=True)),
            ],
            options={
                'db_table': 't_sec_img_details',
            },
        ),
        migrations.CreateModel(
            name='TSecondGoodHouse',
            fields=[
                ('source2_good_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 't_second_good_house',
            },
        ),
        migrations.CreateModel(
            name='TSecondHandTransaction',
            fields=[
                ('sec_id', models.AutoField(primary_key=True, serialize=False)),
                ('deposit_amount', models.FloatField()),
                ('deposit_date', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 't_second_hand_transaction',
            },
        ),
        migrations.CreateModel(
            name='TSecondSource',
            fields=[
                ('source2_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, null=True)),
                ('img_url', models.CharField(max_length=255, null=True)),
                ('pub_date', models.DateTimeField(null=True)),
                ('nearby', models.CharField(max_length=50, null=True)),
                ('region', models.CharField(max_length=50, null=True)),
                ('hu_type', models.CharField(max_length=50, null=True)),
                ('price_s', models.IntegerField(null=True)),
                ('comm_name', models.CharField(max_length=30, null=True)),
                ('area', models.FloatField(null=True)),
                ('sum_price', models.FloatField(null=True)),
                ('dis_price', models.FloatField(null=True)),
                ('sell_rent', models.CharField(max_length=30, null=True)),
                ('rent_money', models.FloatField(null=True)),
                ('face', models.CharField(max_length=30, null=True)),
                ('details', models.CharField(max_length=50, null=True)),
                ('floors', models.IntegerField(null=True)),
                ('k_time', models.DateTimeField(null=True)),
                ('ch_state', models.IntegerField(null=True)),
                ('is_check', models.IntegerField(null=True)),
                ('fav_num', models.IntegerField(null=True)),
                ('comment_num', models.IntegerField(null=True)),
                ('shared_num', models.IntegerField(null=True)),
                ('broker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.TBroker')),
                ('ld', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.TLandlord')),
            ],
            options={
                'db_table': 't_second_source',
            },
        ),
        migrations.CreateModel(
            name='TSelectRentalHouse',
            fields=[
                ('sselect_good_id', models.AutoField(primary_key=True, serialize=False)),
                ('source2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.TSecondSource')),
            ],
            options={
                'db_table': 't_select_rental_house',
            },
        ),
        migrations.CreateModel(
            name='TServ',
            fields=[
                ('serv_id', models.AutoField(primary_key=True, serialize=False)),
                ('ser_user', models.CharField(max_length=50, null=True)),
                ('ser_pwd', models.CharField(max_length=50, null=True)),
                ('ser_phone', models.CharField(max_length=50, null=True)),
                ('login_state', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 't_serv',
            },
        ),
        migrations.CreateModel(
            name='TSource',
            fields=[
                ('source_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('img_url', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField()),
                ('nearby', models.CharField(max_length=255, null=True)),
                ('region', models.CharField(max_length=30)),
                ('hu_type', models.CharField(max_length=30, null=True)),
                ('price_s', models.FloatField(null=True)),
                ('comm_name', models.CharField(max_length=30, null=True)),
                ('area', models.FloatField(null=True)),
                ('sum_price', models.FloatField(null=True)),
                ('dis_price', models.FloatField(null=True)),
                ('face', models.CharField(max_length=30, null=True)),
                ('details', models.CharField(max_length=255, null=True)),
                ('floors', models.IntegerField(null=True)),
                ('k_time', models.DateTimeField(null=True)),
                ('ch_state', models.IntegerField(null=True)),
                ('is_check', models.IntegerField(null=True)),
                ('broker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.TBroker')),
            ],
            options={
                'db_table': 't_source',
            },
        ),
        migrations.CreateModel(
            name='TSup',
            fields=[
                ('sup_id', models.AutoField(primary_key=True, serialize=False)),
                ('sup_user', models.CharField(max_length=50)),
                ('sup_pwd', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 't_sup',
            },
        ),
        migrations.CreateModel(
            name='TUser',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('sex', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('avatar_path', models.CharField(max_length=255, null=True)),
                ('u_name', models.CharField(max_length=50)),
                ('u_pwd', models.CharField(max_length=255)),
                ('status', models.IntegerField()),
                ('balance', models.FloatField()),
                ('regi_date', models.DateTimeField()),
                ('last_date', models.DateTimeField(null=True)),
                ('times', models.IntegerField(null=True)),
                ('code', models.CharField(max_length=20, null=True)),
                ('code_num', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 't_user',
            },
        ),
        migrations.CreateModel(
            name='TUserComment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('comment_type', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
            ],
            options={
                'db_table': 't_user_comment',
            },
        ),
        migrations.CreateModel(
            name='TUserFavourity',
            fields=[
                ('fav_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(null=True)),
                ('source', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.TSource')),
                ('source2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.TSecondSource')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.TUser')),
            ],
            options={
                'db_table': 't_user_favourity',
            },
        ),
        migrations.CreateModel(
            name='TUserHistory',
            fields=[
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(null=True)),
                ('source', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.TSource')),
                ('source2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.TSecondSource')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.TUser')),
            ],
            options={
                'db_table': 't_user_history',
            },
        ),
        migrations.CreateModel(
            name='TUserIntegral',
            fields=[
                ('integ_id', models.AutoField(primary_key=True, serialize=False)),
                ('integral', models.IntegerField(null=True)),
                ('vip_grade', models.IntegerField(db_column='VIP_grade', null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.TUser')),
            ],
            options={
                'db_table': 't_user_integral',
            },
        ),
        migrations.CreateModel(
            name='TUserLd',
            fields=[
                ('user_ld_id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(null=True)),
                ('date', models.DateTimeField(null=True)),
                ('ld', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.TLandlord')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.TUser')),
            ],
            options={
                'db_table': 't_user_ld',
            },
        ),
        migrations.CreateModel(
            name='TUserPost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('date', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.TUser')),
            ],
            options={
                'db_table': 't_user_post',
            },
        ),
        migrations.CreateModel(
            name='TUserRecharge',
            fields=[
                ('recharge_id', models.AutoField(primary_key=True, serialize=False)),
                ('recharge_type', models.CharField(max_length=50, null=True)),
                ('recharge_amount', models.FloatField()),
                ('date', models.DateTimeField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.TUser')),
            ],
            options={
                'db_table': 't_user_recharge',
            },
        ),
        migrations.CreateModel(
            name='TUserServ',
            fields=[
                ('user_serv_id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(null=True)),
                ('date', models.DateTimeField(null=True)),
                ('serv', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.TServ')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.TUser')),
            ],
            options={
                'db_table': 't_user_serv',
            },
        ),
        migrations.CreateModel(
            name='TUserShare',
            fields=[
                ('share_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(null=True)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.TSource')),
                ('source2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.TSecondSource')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.TUser')),
            ],
            options={
                'db_table': 't_user_share',
            },
        ),
        migrations.CreateModel(
            name='TUserVip',
            fields=[
                ('vip_id', models.AutoField(primary_key=True, serialize=False)),
                ('vip_grade', models.IntegerField(db_column='VIP_grade', null=True)),
                ('integral', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 't_user_VIP',
            },
        ),
        migrations.CreateModel(
            name='TWheelPic',
            fields=[
                ('wheel_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, null=True)),
                ('house_url', models.CharField(max_length=255, null=True)),
                ('link', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 't_wheel_pic',
            },
        ),
        migrations.AddField(
            model_name='tusercomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.TUserPost'),
        ),
        migrations.AddField(
            model_name='tusercomment',
            name='source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.TSource'),
        ),
        migrations.AddField(
            model_name='tusercomment',
            name='source2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.TSecondSource'),
        ),
        migrations.AddField(
            model_name='tusercomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.TUser'),
        ),
        migrations.AddField(
            model_name='tsecondhandtransaction',
            name='source2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.TSecondSource'),
        ),
        migrations.AddField(
            model_name='tsecondhandtransaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.TUser'),
        ),
        migrations.AddField(
            model_name='tsecondgoodhouse',
            name='source2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.TSecondSource'),
        ),
        migrations.AddField(
            model_name='tsecimgdetails',
            name='source2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.TSecondSource'),
        ),
        migrations.AddField(
            model_name='treportcomplaints',
            name='source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.TSource'),
        ),
        migrations.AddField(
            model_name='treportcomplaints',
            name='source2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.TSecondSource'),
        ),
        migrations.AddField(
            model_name='treportcomplaints',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.TUser'),
        ),
        migrations.AddField(
            model_name='trentaltransaction',
            name='source2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.TSecondSource'),
        ),
        migrations.AddField(
            model_name='trentaltransaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.TUser'),
        ),
        migrations.AddField(
            model_name='tnewtransaction',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.TSource'),
        ),
        migrations.AddField(
            model_name='tnewtransaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.TUser'),
        ),
        migrations.AddField(
            model_name='tnewimgdetails',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.TSource'),
        ),
        migrations.AddField(
            model_name='tforwardnews',
            name='sup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.TSup'),
        ),
        migrations.AddField(
            model_name='tforwardnews',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.TUser'),
        ),
        migrations.AddField(
            model_name='tcommunity',
            name='source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.TSource'),
        ),
        migrations.AddField(
            model_name='tcheckhousetie',
            name='pt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.TPtAdmin'),
        ),
        migrations.AddField(
            model_name='tcheckhousetie',
            name='source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.TSource'),
        ),
        migrations.AddField(
            model_name='tcheckhousetie',
            name='source2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.TSecondSource'),
        ),
        migrations.AddField(
            model_name='tbroker',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.TCompany'),
        ),
        migrations.AddField(
            model_name='tadnews',
            name='sup',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.TSup'),
        ),
        migrations.AddField(
            model_name='tadcheckrecord',
            name='pt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.TPtAdmin'),
        ),
        migrations.AddField(
            model_name='tad',
            name='ad_bm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.TAdBm'),
        ),
        migrations.AddField(
            model_name='tad',
            name='ad_pos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.TAdPos'),
        ),
    ]
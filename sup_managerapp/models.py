from django.db import models
from django.utils import timezone
# Create your models here.

from mainapp.models import TAdBm,TPtAdmin,TSup,TServ,TUser,TBroker,TCompany,TLandlord,TSecondSource,TSource
class T_Sys_Role(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=30, null=True)
   type = models.CharField(max_length=30,null=True)
   class Meta:
      db_table = 't_sys_role'


class TMessage(models.Model):
   message_id = models.AutoField(primary_key=True)
   title = models.CharField(max_length=50, blank=True, null=True)
   content = models.TextField(blank=True, null=True)
   create_time = models.DateTimeField(default =timezone.now)

   class Meta:
      db_table = 't_message'
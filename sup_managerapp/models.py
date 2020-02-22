from django.db import models

# Create your models here.

from mainapp.models import TAdBm,TPtAdmin,TSup,TServ
class T_Sys_Role(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=30, null=True)
   type = models.CharField(max_length=30,null=True)
   class Meta:
      db_table = 't_sys_role'
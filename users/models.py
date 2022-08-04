from socket import RDS_CMSG_RDMA_UPDATE
from django.db import models
from django.contrib.auth.models import User
import datetime

class User(models.Model):
    user_id = models.OneToOneField(User,on_delete=models.CASCADE,related_name="user") #장고 내장 User 사용
    is_renting = models.BooleanField(default=False)
    left_time = models.DurationField(default=datetime.timedelta())
    ## left_money -> 이건 left_time만 해도 충분할듯?
# Create your models here.

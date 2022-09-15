from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_init, post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import datetime


class Profile(models.Model):
    user_id = models.OneToOneField(User,on_delete=models.CASCADE,related_name="user",primary_key=True) #장고 내장 User 사용
    is_renting = models.BooleanField(default=False)
    left_time = models.DurationField(default=datetime.timedelta())
    
    def borrow_umbrella(self):
        self.is_renting = True

    def return_umbrella(self):
        self.is_renting = False
        
    ## left_money -> 이건 left_time만 해도 충분할듯?


#계정 만들때 profile 자동생성
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance=None, created=False, **kwargs):
    if created:
        Profile.objects.create(user_id=instance)

#계정 생성 시 토큰 생성
@receiver(post_init, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
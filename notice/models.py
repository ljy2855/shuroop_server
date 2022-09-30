from operator import mod
from django.db import models
from rentals.models import Record
from users.models import Profile

from django.dispatch import receiver
from django.db.models.signals import post_save

class NoticeType(models.TextChoices):
    NEW_RENTAL = 'new_rental'
    CLOSE_RENTAL = 'close_rental',
    OVER_RENTAL_TIME = 'over_rental_time'
    COME_UP_RETURN = 'come_up_return'
    WEATHER_NOTICE = 'weather_notice'
    

class Notification(models.Model):
    notice_type = models.CharField(max_length=20,choices=NoticeType.choices,default=None)
    content = models.TextField(max_length=50,)
    profile_id = models.ForeignKey(Profile,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

@receiver(post_save,sender=Record)
def create_rental_notice(sender, instance, created, **kwargs):
    if created == True: #대여 시
        record = instance
        borrow_time_format = record.get_borrow_time_format()
        content = borrow_time_format+"에 대여했어요! 24시간 내로 반납하는 것을 잊지 마세요."
        Notification.objects.create(
            notice_type=NoticeType.NEW_RENTAL,
            profile_id=record.user,
            content=content
        )
    else: #반납 시
        record = instance
        if record.check_over_time():
            content = "반납이 완료되었어요!"
            Notification.objects.create(
                notice_type=NoticeType.CLOSE_RENTAL,
                profile_id=record.user,
                content=content,
            )

        



# Create your models here.

import datetime
from django.db import models


from users.models import Profile


class Position(models.Model):
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)

class Place(models.Model):
    name = models.CharField(max_length=30)
    position = models.OneToOneField(Position,on_delete=models.CASCADE,null=False,related_name='position')
    umbrella_count = models.IntegerField(default=0)
    address = models.CharField(max_length=30,null=True)
    max_count = models.IntegerField()
    is_empty = models.BooleanField()
    is_full = models.BooleanField()
    description = models.CharField(max_length=30)
    def borrow_item(self):
        self.umbrella_count = self.umbrella_count -1
        self.save()

    def return_item(self):
        self.umbrella_count = self.umbrella_count + 1
        self.save()

    def save(self, *args, **kwargs):
        if self.max_count is self.umbrella_count:
            self.is_full = True
        else:
            self.is_full = False
        if self.umbrella_count is 0:
            self.is_empty = True
        else:
            self.is_empty = False
        super(Place, self).save(*args, **kwargs)

class Record(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,null=False)
    is_renting = models.BooleanField(default=True)
    borrow_time = models.DateTimeField(auto_now_add=True)
    borrow_place = models.ForeignKey(Place,on_delete=models.SET_NULL,null=True,related_name='borrow_place')
    return_time = models.DateTimeField(null=True)
    return_place = models.ForeignKey(Place,on_delete=models.SET_NULL,null=True,related_name='return_place')
    over_time = models.DurationField(default=datetime.timedelta())
    charge = models.IntegerField(default=0)

    def close_rental(self,place) -> None:
        self.is_renting = False
        self.return_time = datetime.datetime.now()
        self.return_place = place
        rental_time = self.return_time - self.borrow_time
        if rental_time > datetime.timedelta(day=1):
            self.over_time = rental_time - datetime.timedelta(day=1)
        self.save()

    def get_borrow_time_format(self) -> str:
        return self.borrow_time.strftime("%-m월 %-d일 %A %p %-H시 %-M분")

    def check_over_time(self) ->bool:
        if self.over_time > datetime.timedelta():
            return True
        return False




# Create your models here.

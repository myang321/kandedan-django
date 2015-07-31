from django.db import models


# Create your models here.
class Users(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=50)
    screen_name = models.CharField(max_length=30)
    user_type = models.CharField(max_length=30, default='normal')
    group = models.ForeignKey('kandedan.Groups', null=True)

    @classmethod
    def create(cls, username, password, uid=None, screen_name=None, user_type='normal', group_id=None):
        if screen_name is None:
            screen_name = username
        user = cls(username=username, password=password, uid=uid, screen_name=screen_name, user_type=user_type,
                   group_id=group_id)
        return user


class Balance(models.Model):
    class Meta:
        unique_together = (('creditor', 'debtor'),)

    creditor = models.CharField(max_length=30, primary_key=True)
    debtor = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2)


class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users)
    trans_type = models.CharField(max_length=30)
    message = models.CharField(max_length=1000, default='')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.CharField(max_length=30, default='')


class Trans_detail(models.Model):
    id = models.AutoField(primary_key=True)
    debtor = models.ForeignKey(Users)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    percent = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    trans = models.ForeignKey(Transaction)


class Groups(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    holder = models.ForeignKey(Users)

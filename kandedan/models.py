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

    def __str__(self):
        str1 = "User Object:\nusername:{0} screen_name:{1}\n\n".format(self.username, self.screen_name)
        return str1


class Balance(models.Model):
    creditor = models.CharField(max_length=30, primary_key=True)
    debtor = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "Balance Object\ncreditor:{0} debtor:{1} amount:{2}\n".format(self.creditor, self.debtor, self.amount)

    class Meta:
        unique_together = (('creditor', 'debtor'),)


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


class UserBalance(object):
    def __init__(self, username):
        self.username = username
        self.creditor_list = []

    def add_balance(self, balance):
        self.creditor_list.append(balance)

    def __str__(self):
        str1 = "UserBalance Object:\n"
        str1 += "Username={0}\n".format(self.username)
        for c in self.creditor_list:
            str1 += "   debtor:{0}, ${1}\n".format(c.creditor, c.amount)
        return str1

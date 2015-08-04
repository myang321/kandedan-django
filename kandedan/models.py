from django.db import models
from .const import *


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
    who = []

    # def __init__(self, *args, **kwargs):
    #     # call super before assign anything
    #     super(Transaction, self).__init__(*args, **kwargs)
    #     user = kwargs.pop('user', None)
    #     trans_type = kwargs.pop('trans_type', None)
    #     message = kwargs.pop('message', None)
    #     amount = kwargs.pop('amount', None)
    #     date = kwargs.pop('date', None)
    #     who = kwargs.pop('who', None)
    #     if user is not None:
    #         who_list2, message2 = Transaction._process_who_list(who, message, amount)
    #         self.user = user
    #         self.trans_type = trans_type
    #         self.message = message2
    #         self.amount = amount
    #         self.date = date
    #         self.who = who_list2

    @staticmethod
    def _process_who_list(who_list, message, amount):
        sum1 = 0
        cnt = 0
        str1 = LINE_SEPARATOR + " shared with "
        who_list2 = []
        for u in who_list:
            sum1 += u[1]
            if cnt > 0:
                str1 += ','
            str1 += u[0]
            if u[1] > 1:
                str1 += '*' + str(u[1])
            cnt += 1
        message += str1
        amount_per_unit = amount / sum1
        for u in who_list:
            tuple1 = (u[0], amount_per_unit * u[1])
            who_list2.append(tuple1)
        return who_list2, message

    # for type: buy
    @classmethod
    def create(cls, user, trans_type, message, amount, date, who):
        who_list2, message2 = Transaction._process_who_list(who, message, amount)
        # do not pass transient field into constructor
        trans = Transaction(user=user, trans_type=trans_type, message=message2, amount=amount, date=date)
        trans.who = who_list2
        return trans

    def split_msg(self):
        return self.message.split(LINE_SEPARATOR)


class Trans_detail(models.Model):
    id = models.AutoField(primary_key=True)
    debtor = models.ForeignKey(Users)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    percent = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    trans = models.ForeignKey(Transaction)

    @classmethod
    def create(cls, debtor, amount, trans):
        trans_detail = Trans_detail(debtor=debtor, amount=amount, trans=trans)
        return trans_detail


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

__author__ = 'Steve'
import django
from .models import Users, Groups, Transaction, Trans_detail, Balance, UserBalance
from .const import *
import decimal


def user_authentication(username, password):
    user = Users.objects.get(username=username, password=password)
    return user


def get_all_transaction(group_id=None):
    trans = Transaction.objects.filter(group=get_group(group_id)).order_by('-id')
    return trans


def get_all_normal_user_info(group_id=None, username=None):
    if group_id is None and username is None:
        users = Users.objects.all()
    elif group_id is not None:
        users = Users.objects.filter(group_id=group_id)
    else:
        users = Users.objects.filter(username=username)
    return users


def get_creditor_debtor_list(group_id=None):
    users = get_all_normal_user_info(group_id)
    ub_list = []
    for u in users:
        ub = UserBalance(u.username)
        balances = Balance.objects.filter(debtor=u.username)
        for b in balances:
            ub.add_balance(b)
        ub_list.append(ub)
    return ub_list


def add_trans_detail(trans, debtor, amount):
    user = get_user(debtor)
    trans_detail = Trans_detail.create(debtor=user, amount=amount, trans=trans)
    trans_detail.save()


def get_balance(creditor, debtor):
    balance = Balance.objects.get(creditor=creditor, debtor=debtor)
    return balance.amount


def get_screen_name(username):
    user = Users.objects.get(username=username)
    return user.screen_name


def update_balance(creditor, debtor, amount):
    balance = Balance.objects.get(creditor=creditor, debtor=debtor)
    balance.amount = amount
    balance.save()


def append_transaction_message(trans, message):
    message = LINE_SEPARATOR + message
    trans.message += message
    trans.save()


# money goes to creditor
# 1. debtor active pay
# 2. debtor passive pay (debtor buy sth)
def change_balance(creditor, debtor, amount, trans):
    amount = decimal.Decimal(amount)
    current = get_balance(creditor, debtor)
    current2 = get_balance(debtor, creditor)
    creditor_name = get_screen_name(creditor)
    debtor_name = get_screen_name(debtor)
    if current == 0:
        remain = current2 + amount
        update_balance(debtor, creditor, remain)
        msg = "{0} owe {1} from ${2:.2f} to ${3:.2f}".format(creditor_name, debtor_name, current2, remain)
    elif current >= amount:
        remain = current - amount
        update_balance(creditor, debtor, remain)
        msg = "{0} owe {1} from ${2:.2f} to ${3:.2f}".format(debtor_name, creditor_name, current, remain)
    else:
        remain = amount - current
        update_balance(creditor, debtor, 0)
        update_balance(debtor, creditor, remain)
        msg = "{0} owe {1} from ${2:.2f} to ${3:.2f}".format(creditor_name, debtor_name, -current, remain)
    print("in change balance ", msg)
    append_transaction_message(trans, msg)


def get_user(username):
    user = Users.objects.get(username=username)
    return user


def get_group(group_id):
    group = Groups.objects.get(id=group_id)
    return group


def save_transaction(username, amount, date, message, who, trans_type, group_id):
    user = get_user(username)
    trans = Transaction.create(user=user, trans_type=trans_type, message=message, amount=amount, date=date, who=who,
                               group=get_group(group_id))
    trans.save()
    if trans.trans_type == TRANS_TYPE_BUY:
        for u in trans.who:
            debtor = u[0]
            indi_amount = u[1]
            add_trans_detail(trans, debtor, indi_amount)
            if debtor == username:
                continue
            print("in save trans: debtor", debtor)
            change_balance(debtor, username, indi_amount, trans)
    elif trans.type == TRANS_TYPE_PAY:
        pass


if __name__ == '__main__':
    django.setup()
    from kandedan.models import Users, Groups, Transaction, Trans_detail, Balance

    print(Users.objects.all())
    # u = Users(username='meng', password='123')

__author__ = 'Steve'
import django
from .models import Users, Groups, Transaction, Trans_detail, Balance, UserBalance


def user_authentication(username, password):
    user = Users.objects.get(username=username, password=password)
    return user


def get_all_transaction(group_id=None, username=None):
    trans = Transaction.objects.all()
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


if __name__ == '__main__':
    django.setup()
    from kandedan.models import Users, Groups, Transaction, Trans_detail, Balance

    print(Users.objects.all())
    # u = Users(username='meng', password='123')

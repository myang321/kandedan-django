__author__ = 'Steve'
import django
from .models import Users, Groups, Transaction, Trans_detail, Balance


def user_authentication(username, password):
    user = Users.objects.get(username=username, password=password)
    return user


def get_all_transaction(group_id=None, username=None):
    trans = Transaction.objects.all()
    return trans


def get_creditor_debtor_list(con, group_id=None):
    balances = Balance.objects.all()
    return None


if __name__ == '__main__':
    django.setup()
    from kandedan.models import Users, Groups, Transaction, Trans_detail, Balance

    print(Users.objects.all())
    # u = Users(username='meng', password='123')

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from . import database_util as db

SESSION_NAME = 'name'
SESSION_SCREEN_NAME = 'screen_name'
SESSION_GROUP_ID = 'group_id'
SESSION_USER_TYPE = 'user_type'

USER_TYPE_SUPER = 'super'
USER_TYPE_NORMAL = 'normal'


# Create your views here.
def login(request):
    if request.session.get(SESSION_NAME):
        return HttpResponseRedirect(reverse('main'))
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = db.user_authentication(username, password)
        if user is not None:
            request.session[SESSION_NAME] = username
            request.session[SESSION_SCREEN_NAME] = user.screen_name
            request.session[SESSION_GROUP_ID] = user.group_id
            request.session[SESSION_USER_TYPE] = user.user_type
            return HttpResponseRedirect(reverse('main'))
    else:
        context = {}
        return render(request, 'kandedan/login.html', context)


def main(request):
    if not request.session.get(SESSION_NAME):
        return HttpResponseRedirect(reverse('login'))
    trans = db.get_all_transaction(request.session.get(SESSION_GROUP_ID), request.session.get(SESSION_NAME))
    balances = None
    not_in_group_msg = None
    if request.session[SESSION_GROUP_ID] != 0:
        balances = db.get_creditor_debtor_list(request.session[SESSION_GROUP_ID])
    else:
        not_in_group_msg = "You are not in any group, please create or join a group in Setting page."
    context = {'trans': trans, 'balances': balances, 'not_in_group_msg': not_in_group_msg,
               'request': request}
    return render(request, 'kandedan/main.html', context)


def logout(request):
    request.session.clear()
    return HttpResponseRedirect(reverse('login'))

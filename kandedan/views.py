from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from . import database_util as db
from .const import *


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
    trans = db.get_all_transaction(request.session.get(SESSION_GROUP_ID))
    ub_list = None
    not_in_group_msg = None
    if request.session[SESSION_GROUP_ID] != 0:
        ub_list = db.get_creditor_debtor_list(request.session[SESSION_GROUP_ID])
    else:
        not_in_group_msg = "You are not in any group, please create or join a group in Setting page."
    context = {'trans': trans, 'ub_list': ub_list, 'not_in_group_msg': not_in_group_msg,
               'request': request}
    return render(request, 'kandedan/main.html', context)


def logout(request):
    request.session.clear()
    return HttpResponseRedirect(reverse('login'))


def add(request):
    if not request.session.get(SESSION_NAME):
        return HttpResponseRedirect(reverse('main'))
    if request.method == 'POST':
        amount = float(request.POST['amount'])
        date = request.POST['date']
        msg = request.POST['msg']
        who = request.POST.getlist('who')
        who_tuple_list = []
        for u in who:
            cnt = int(request.POST['cnt' + u])
            tuple1 = (u, cnt)
            who_tuple_list.append(tuple1)
        db.save_transaction(username=request.session[SESSION_NAME], amount=amount, date=date, message=msg,
                            who=who_tuple_list, trans_type=TRANS_TYPE_BUY, group_id=request.session[SESSION_GROUP_ID])
        return HttpResponseRedirect(reverse('main'))
    else:
        users = db.get_all_normal_user_info(request.session[SESSION_GROUP_ID])
        context = {'users': users}
        return render(request, 'kandedan/add.html', context)

from django.core.paginator import Paginator
from django.db.models import Q, Count, Sum, Avg, Min, Max
from django.shortcuts import render, redirect

from .models import Friend
from .forms import FriendForm, FindForm, CheckForm


def index(request, num=1):
    data = Friend.objects.all()
    page = Paginator(data, 3)
    params = {
        'title': 'Hello',
        'message': '',
        'data': page.get_page(num),
    }
    return render(request, 'hello/index.html', params)


# create model
def create(request):
    if request.method == 'POST':
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'form': FriendForm(),
    }

    return render(request, 'hello/create.html', params)


def edit(request, num):
    obj = Friend.objects.get(id=num)
    if request.method == 'POST':
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')

    params = {
        'title': 'Hello',
        'id': num,
        'form': FriendForm(instance=obj)
    }
    return render(request, 'hello/edit.html', params)


def delete(request, num):
    friend = Friend.objects.get(id=num)
    if request.method == 'POST':
        friend.delete()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'id': num,
        'obj': friend,
    }
    return render(request, 'hello/delete.html', params)


def find(request):
    if request.method == 'POST':
        msg = request.POST['find']
        form = FindForm(request.POST)
        sql = 'select * from hello_friend'
        if msg != '':
            sql += ' where ' + msg
        data = Friend.objects.raw(sql)
        msg = sql
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'message': msg,
        'form': form,
        'data': data,
    }
    return render(request, 'hello/find.html', params)


def check(request):
    params = {
        'title': 'Hello',
        'message': 'check validation. ',
        'form': CheckForm(),
    }
    if request.method == 'POST':
        obj = Friend()
        form = FriendForm(request.POST, instance=obj)
        params['form'] = form
        if form.is_valid():
            params['message'] = 'OK!'
        else:
            params['message'] = 'no good.'
    return render(request, 'hello/check.html', params)

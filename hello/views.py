from django.db.models import Q
from django.shortcuts import render, redirect

from .models import Friend
from .forms import FriendForm, FindForm


def index(request):
    data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'data': data,
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
        msg = 'search result:'
        form = FindForm(request.POST)
        str = request.POST['find']
        val = str.split()
        data = Friend.objects.filter(Q(name__contains=str) \
                                     | Q(mail__contains=str))
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

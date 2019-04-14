from django.db.models import QuerySet
from django.shortcuts import render
from .models import Friend


def __new_str__(self):
    result = ''
    for item in self:
        result += "<tr>"
        for k in item:
            result += '<td>' + str(k) + '=' + str(item[k]) + '</td>'
        result += '</tr>'
    return result


QuerySet.__str__ = __new_str__


def index(request):
    data = Friend.objects.all().values('id', 'name', 'age')
    params = {
        'title': 'Hello',
        'data': data,
    }
    return render(request, 'hello/index.html', params)

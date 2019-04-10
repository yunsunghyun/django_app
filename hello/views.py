from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend
from .forms import HelloForm

def index(request):
    params = {
        'title' : 'Hello',
        'message' : 'all friends. ',
        'form' : HelloForm(),
        'data' : [],
    }
    if (request.method == 'POST'):
        num = request.POST['id']
        item = Friend.objects.get(id=num)
        params['data'] = [item]
        params['form'] = HelloForm(request.POST)
    else:
        params['data'] = Friend.objects.all()
    return render(request, 'hello/index.html', params)





##########################################################
# from django.shortcuts import render
# from django.http import HttpRequest
# from django.views.generic import TemplateView
# from .forms import HelloForm

# class HelloView(TemplateView):

#     def __init__(self):
#         self.params = {
#             'title' : 'Hello',
#             'form' : HelloForm(),
#             'result' : None
#         }

#     def get(self, request):
#         return render(request, 'hello/index.html', self.params)

#     def post(self, request):
#         ch = request.POST.getlist('choice')
#         result = '<ol><b>selected:</b>'
#         for item in ch:
#             result += '<li>' + item + '</li>'
#         result += '</ol>'
#         self.params['result'] = result
#         self.params['form'] = HelloForm(request.POST)
#         return render(request, 'hello/index.html', self.params)

    # def post(self, request):
    #     chk = request.POST['check']
    #     self.params['result'] = 'you selected: "' + chk + '".'
    #     self.params['form'] = HelloForm(request.POST)
    #     return render(request, 'hello/index.html', self.params)

############################################################################################
    # def __init__(self):
    #     self.parmas = {
    #         'title' : 'Hello',
    #         'message' : 'your data:',
    #         'form' : HelloForm()
    #     }
    
    # def get(self, request):
    #     return render(request, 'hello/index.html', self.parmas)

    # def post(self, request):
    #     msg = 'あなたは、<b>' + request.POST['name'] + \
    #         ' (' + request.POST['age'] + \
    #         ') </b>さんです。<br>メールアドレスは <b>' + request.POST['mail'] + \
    #         '</b> ですね。'
    #     self.parmas['message'] = msg
    #     self.parmas['form'] = HelloForm(request.POST)
    #     return render(request, 'hello/index.html', self.parmas)
############################################################################################

# def index(request):
#     if 'msg' in request.GET:
#         msg = request.GET['msg']
#         result = 'you typed:"' + msg + '".'
#     else:
#         return HttpResponse('please send msg parameter!')
#     msg = request.GET['msg']
#     return HttpResponse(result)

# def index(request, id, nickname):
#     result = 'your id: ' + str(id) + ', name: "' \
#         + nickname + '".'
#     return HttpResponse(result) 

# def index(request):
#     return render(request, 'hello/index.html')

# def index(request):
#     params = {
#         'title' : 'Hello',
#         'message' : 'your data: ',
#         'form' : HelloForm()
#     }
#     if (request.method == 'POST'):
#         params ['message'] = '名前 : ' + request.POST['name'] + \
#             '<br>メール : ' + request.POST['mail'] + \
#             '<br>年齢 : ' + request.POST['age']
#         params['form'] = HelloForm(request.POST)
#     return render(request, 'hello/index.html', params)

# def next(request):
#     params = {
#         'title' : 'Hello/Next',
#         'msg' : 'これは、もう１つのページです。',
#         'goto' : 'index',
#     }  
#     return render(request, 'hello/index.html', params)

# def form(request):
#     msg = request.POST['msg']
#     params = {
#         'title' : 'Hello/Form',
#         'msg' : 'こんにちは、' + msg + 'さん。',
#         'goto' : 'index',
#     }
#     return render(request, 'hello/index.html', params)
# Create your views here.

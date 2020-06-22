from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext


# render login page
def index_view(request):
    return render(request, 'login.html')


# deploy log in
def login_view(request):
    # Get form request args
    uname = request.POST.get('uname', '')
    pwd = request.POST.get('pwd')

    if uname == 'David' and pwd == '123':
        return HttpResponse('logged in')

    return HttpResponse('Fail')

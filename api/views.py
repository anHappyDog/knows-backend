import json
import os.path

from django.conf.global_settings import MEDIA_ROOT
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password, check_password
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from api.models import User
from django.contrib.sessions.models import Session
from django.middleware.csrf import get_token


@csrf_exempt
@require_http_methods('POST')
def uploadImg(request):
    receivedFile = request.FILES.get("file")
    print(receivedFile.name)
    filename = os.path.join(MEDIA_ROOT, receivedFile.name)
    with open(filename, 'wb') as f:
        f.write(receivedFile.read())
    return JsonResponse({"status": 0})


@require_http_methods('GET')
def getCsrfToken(request):
    return JsonResponse({"csrfToken": get_token(request)})


# Create your views here.
@require_http_methods('GET')
def getInfo(request):
    return 10


@require_http_methods('GET')
def validSessionToken(request):
    get_token(request)
    sessionId = request.COOKIES.get("sessionid")
    if sessionId:
        try:
            session = Session.objects.get(session_key=sessionId)
            sessionData = session.get_decoded()
            if sessionData['is_authenticated']:
                return JsonResponse({"status": 0})
        except Session.DoesNotExist:
            return JsonResponse({"status": -1})
    return JsonResponse({"status": -1})


# 0代表已经认证
# -1代表并没有


@require_http_methods('POST')
def signUp(request):
    get_token(request)
    response = {}
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    email = data['email']
    phone = data['phone']
    result = User.objects.filter(username=username)
    if len(result) != 0:
        response['status'] = -1
    else:
        User(username=username, password=password, email=email, phone=phone).save()
        response['status'] = 0
    return JsonResponse(response)


@require_http_methods('POST')
def signIn(request):
    if "HTTP_X_CSRFTOKEN" in request.META:
        csrf_token = request.META['HTTP_X_CSRFTOKEN']
        print(csrf_token)
    sessionId = request.COOKIES.get("sessionid")
    if sessionId:
        try:
            session = Session.objects.get(session_key=sessionId)
            sessionData = session.get_decoded()
            if sessionData['is_authenticated']:
                return JsonResponse({"status": 0})
        except Session.DoesNotExist:
            pass
    response = {}
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    result = User.objects.filter(username=username)
    if len(result) == 0:
        response['status'] = -1
    elif len(result) != 1:
        response['status'] = -3
    elif check_password(password, result[0].password):
        response['status'] = 0
        request.session['is_authenticated'] = True
        request.session['username'] = username
    else:
        response['status'] = -2
    return JsonResponse(response)

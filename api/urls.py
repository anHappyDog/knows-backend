from django.urls import path
from .views import signIn, signUp, validSessionToken, getCsrfToken,uploadImg

urlpatterns = [
    path('signIn', signIn),
    path('signUp', signUp),
    path('validSessionToken', validSessionToken),
    path('getCsrfToken', getCsrfToken),
    path('uploadImg',uploadImg),
]

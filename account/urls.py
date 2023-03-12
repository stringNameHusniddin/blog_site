from django.urls import path
from .views import SignUpPage

urlpatterns = [
    path('signup/', SignUpPage.as_view(), name='signup')
]
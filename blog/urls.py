from django.urls import path
from .views import HomePage, DetailPage, NewBlogPage, UpdatePage, DeletePage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('blog/<int:pk>', DetailPage.as_view(), name='detail'),
    path('blog/new/', NewBlogPage.as_view(), name='new'),
    path('blog/update/<int:pk>', UpdatePage.as_view(), name='update'),
    path('blog/delete/<int:pk>', DeletePage.as_view(), name='delete')
]
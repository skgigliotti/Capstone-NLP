from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/detail', views.detail, name='detail'),
    path('form/', views.box_view, name='form'),
]

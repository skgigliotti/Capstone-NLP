from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/detail', views.detail, name='detail'),
    path('form/', views.text_view, name='form'),
    path('results/<int:question_id>/', views.results, name='results'),
    path('results/index/',views.index, name='index'),
]

from django.contrib import admin
from django.urls import path,include
from cricket import views

urlpatterns = [
    path('',  views.team_list,name='team_list'),
    path('team_detail/<int:pk>',  views.team_detail,name='team_detail'),
    path('matches',  views.fixture,name='matches'),
    path('points',  views.points_table,name='points'),
]

app_name = 'cricket'
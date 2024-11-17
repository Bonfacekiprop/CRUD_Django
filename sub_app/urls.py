from django.urls import path
from . import views

app_name = 'sub_app'
urlpatterns = [
    path('',views.home,name='home'),
    path('addspkear/',views.addspeaker,name='speaker'),
    path('home/',views.starter,name='mwanzo'),
    path('speaker/',views.speaker,name='ongea'),
] 
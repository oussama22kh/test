from django.urls import path
from sender import views

urlpatterns = [
    path('',views.ReceiverView.as_view(),name='receiver')
]

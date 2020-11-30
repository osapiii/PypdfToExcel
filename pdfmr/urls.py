from django.urls import path 
from . import views

app_name = 'pdfmr'

urlpatterns = [
    path('top',views.TopView.as_view(), name='top')
]

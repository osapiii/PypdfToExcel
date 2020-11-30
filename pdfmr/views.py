from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class TopView(LoginRequiredMixin,View):
    """
    TOPページのビュー
    """
    def get(self,request):
        return render(request,'pdfmr/top.html')
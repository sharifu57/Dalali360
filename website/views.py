from django.shortcuts import render, redirect
from django.views.generic import View
from web.views import *

# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {}

        return render(request, 'pages/index.html')

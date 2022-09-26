from django.shortcuts import render
from django.views.generic import View


# Create your views here.

class RenderViewFrontend(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


def index(request):
    return render(request, 'index.html')

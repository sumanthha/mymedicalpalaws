 # main/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

from django.contrib.auth import authenticate, login

class LoginPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'login.html', context=None)

    def post(self, request, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
        else:
            # Return an 'invalid login' error message.
            pass

def logout_view(request):
    logout(request)
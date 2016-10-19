from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from calculator_app.models import Profile

def operation(num1, num2, sign):
    if sign == '+':
        return num1 + num2
    elif sign == '-':
        return num1 - num2
    elif sign == '*':
        return num1 * num2
    else:
        return num1 / num2


def calculator_view(request):
    if request.GET:
        if request.GET != "" or request.GET == int:
            num1 = int(request.GET['num1'])
            num2 = int(request.GET['num2'])
            sign = request.GET['sign']
    else:
        num1 = 1
        num2 = 1
        sign = 'add'
        print(request.GET)

    context = {
        'n1': num1,
        'n2': num2,
        'sign': sign,
        'solution': operation(num1, num2, sign),
    }
    return render(request, 'calculator.html', context)

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('calculator_view')

class ProfileView(TemplateView):
    template_name = "profile.html"

class ProfileUpdateView(UpdateView):
    model = Profile
    success_url = reverse_lazy('calculator_view')
    fields = ('user_type',)

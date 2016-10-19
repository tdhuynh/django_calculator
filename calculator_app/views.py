from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from calculator_app.models import Profile, Operation


class CalculatorView(CreateView):
    model = Operation
    success_url = reverse_lazy('calculator_view')
    fields = ('num1', 'sign', 'num2')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["operation_list"] = Operation.objects.all()
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('calculator_view')


class ProfileDetailView(DetailView):
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["operation_list"] = Operation.objects.all()
        return context

    def get_queryset(self):
        if  self.request.user.profile.is_owner:
            return Profile.objects.all()
        return Profile.objects.filter(user=self.request.user)


class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ('user_type',)

    def get_success_url(self, **kwargs):
        return reverse_lazy('profile_detail_view', args=[int(self.kwargs['pk'])])

    def get_queryset(self):
        if  self.request.user.profile.is_owner:
            return Profile.objects.all()
        return Profile.objects.filter(user=self.request.user)

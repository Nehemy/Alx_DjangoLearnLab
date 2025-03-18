from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .forms import CustomUserCreationForm

def index(request):
    return render(request, 'blog/index.html')

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')
    
# class ProfileUpdateView(LoginRequiredMixin, UpdateView):
#     model = User
#     fields = ['username', 'email']
#     template_name = 'blog/profile.html'
#     success_url = reverse_lazy('profile')
    
#     def get_object(self, queryset=None):
#         return self.request.user

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)
    
    return render(request, 'blog/profile.html', {'form': form})
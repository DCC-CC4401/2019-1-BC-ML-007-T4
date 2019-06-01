from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import BaseUserCreationForm
from django.views.generic import CreateView, DeleteView
from .models import BaseUser
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse

def landing_page(request, *args):

    return render(request, 'landing_page.html')

def evaluators_page(request, *args):
    form = BaseUserCreationForm
    return render(request, 'evaluators.html', {'form':form})

class registro_usuario(CreateView):
    model = BaseUser 
    template_name = 'evaluators.html'
    form_class = BaseUserCreationForm

    def get_context_data(self, **kwargs):
        ctx = super(registro_usuario,self).get_context_data(**kwargs)
        queryset1 = BaseUser.objects.filter(is_staff=False)
        queryset2=[]
        for user in queryset1:
            queryset2.append(user.id)
        ctx["evaluators"] = zip(queryset1, queryset2)
	
        return ctx

    def form_valid(self, form):
        form.save()
        messages.success(self.request, form['username'].value() +"  "+form['password1'].value())
        return render(self.request, 'evaluators.html', self.get_context_data())
    

class DeleteUserView(SuccessMessageMixin, DeleteView):
	model = BaseUser
	success_url = reverse_lazy('Evaluators Page')
	success_message = "deleted..."
from django.shortcuts import render
from django.contrib.auth.decorators import login_required  #logn line to import this
from testapp.forms import signup
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from testapp.models import company
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
# Create your views here.
def homepage_view(request):
    return render(request,'testapp/home.html')

def mainpage_view(request):
    return render(request,'testapp/mainpage.html')

@login_required    #vaid user can open only
def pythonexam_view(request):
    return render(request,'testapp/pythonexams.html')
@login_required
def javaexam_view(request):
    return render(request,'testapp/javaexams.html')

@login_required
def aptitudeexam_view(request):
    return render(request,'testapp/aptitudeexams.html')

def logout_view(request):
    return render(request,'testapp/logout.html')

@login_required
def CompanyListView(request):
    return render(request,'testapp/company_detail.html')

def signup_view(request):
    form =signup()
    if request.method=='POST':
        form = signup(request.POST)
        #if form.is_valid():
        #    form.save()
        #or
        user = form.save()                #U will not write this code so password will save in encripted format so you will write this code
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})


class CompanyListView(ListView):
    model = company

class CompanyDetailView(DetailView):
    model = company

class CompanyCreateView(CreateView):
    model = company
    fields = ('name','location','ceo')

class CompanyUpdateView(UpdateView):
    model = company
    fields = {'name','ceo'}

class CompanyDeleteView(DeleteView):
    model = company
    success_url=reverse_lazy('companies')

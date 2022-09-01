from dataclasses import field
from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.views.generic import TemplateView,FormView,CreateView,ListView,DetailView,UpdateView,DeleteView 
from classroom.models import Teacher
from classroom.forms import ContactForm #have to import from forms
# Create your views here.
class HomeView(TemplateView):
    template_name='classroom/home.html'
class ThankYouView(TemplateView):
    template_name='classroom/thank_you.html'

class ContactFormView(FormView):
    form_class=ContactForm
    template_name='classroom/contact.html'
    
    # URL not a template.html
    success_url="/classroom/thank_you/"
    #what to do with the form
    def form_valid(self,form):
      print(form.cleaned_data)# return a dictionary of form
      return super().form_valid(form)# similar to formname(request.POST)

class TeacherCreateView(CreateView):
    model=Teacher#to connect the model in class based views
    #model_form.html
    # .save()
    fields="__all__"#include all fields from the model
    success_url=reverse_lazy('classroom:list_teacher')#it does the same as reverse does in function based views

class TeacherListView(ListView):
    #model_list.html
    model=Teacher
    #By default here QuerySet=Teacher.objects.all() can change if u want to
    context_object_name="teacher_list"  
class TeacherDetailView(DetailView):
    #RETURN ONLY ONE MODEL ENTRY PK
    #model_detail.html
    model=Teacher
    #PK-->{{teacher}}
class TeacherUpdateView(UpdateView):
    #SHARE model_form.html--PK
    model=Teacher
    fields="__all__"
    success_url=reverse_lazy('classroom:list_teacher')
class TeacherDeleteView(DeleteView):
    #Form--> Confirm Delete Button
    model=Teacher
    success_url=reverse_lazy('classsroom:list_teacher')

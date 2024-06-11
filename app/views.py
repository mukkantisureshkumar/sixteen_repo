from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from app.forms import *
from django.http import HttpResponse
# Create your views here.
class DataInsertByTv(TemplateView):
    template_name= 'DataInsertByTv.html'

    def get_context_data(self,**kwargs):
        ecdo=super().get_context_data(**kwargs)
        #ecdo['sname']='suresh'
        #ecdo['sage']=23

        ecdo['ecdo']=CollegeForm()
        return ecdo
    def post(self,request):
        collected_data=CollegeForm(request.POST)
        if collected_data.is_valid():
            collected_data.save()
            return HttpResponse('data is inserted')
        else:
            return HttpResponse('data is not inserted')

class DataInsertByFv(FormView):
    template_name='DataInsertByFv.html' 
    form_class=CollegeForm
    def form_valid(self,form):
        form.save()
        return HttpResponse('done !!')

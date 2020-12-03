from django.shortcuts import render
from .models import form_form

# Create your views here.
def index (request):
    if request.method =='POST':
        form_v = form_form(data= request.POST)
        if form_v.is_valid():
            form_v.save(commit = True)
        else :
            print(form_v.errors)
    form_view = form_form()
    return render(request, 'base.html',{"form_view" : form_view})

from django.shortcuts import render
from .models import Details
# Create your views here.


def index(request):

    
     docs = Details.objects.all()
     return render (request,'index.html',{'docs' : docs})
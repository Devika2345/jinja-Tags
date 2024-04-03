from django.shortcuts import render

# Create your views here.
def send_data(request):
    d={'name':'Devika','Age':20}
    return render(request,'send_data.html',context=d)

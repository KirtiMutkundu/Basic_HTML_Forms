from django.shortcuts import render

# Create your views here.
def sample_form(request):
    return render(request,'sample_form.html')
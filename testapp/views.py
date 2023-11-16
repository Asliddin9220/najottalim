from django.shortcuts import render
from django.http import myproject
# Create your views here.
def avtomobiles(request):
    content = myproject.objects.all()
    return render(request=request, context={}, template_name='avto.html', context={'content':content})
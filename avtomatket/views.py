from django.shortcuts import render
from django.http import Avto
# Create your views here.
def avtomobiles(request):
    content = Avto.objects.all()
    return render(request=request, context={}, template_name='avto.html', context={'content':content})
from django.shortcuts import render
from django.http import HttpResponse
from 
# Create your views here.
def index(request):
    post_list = Post.objects.all().order_by('-create_time')
    return render(request, 'index.html', context={'post_list':post_list})
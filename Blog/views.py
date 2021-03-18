from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request, 'Blog/post_list.html',{'posts':posts})


def post_detail(request,pk):
    post= get_object_or_404(Post,pk=pk)
    return render(request,'Blog/post_details.html',{'post':post})

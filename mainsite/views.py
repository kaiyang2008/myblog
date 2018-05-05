from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

from .models import Post

def homepage(request):
    posts = Post.objects.all()
    post_list = list()
    for count,post in enumerate(posts):
        post_list.append("No.{}".format(str(count)) + str(post)+"<br>")
    return HttpResponse(post_list)

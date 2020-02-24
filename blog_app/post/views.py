from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from .models import *
from .forms import *

# Create your views here.
class PostCreate(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'post/create.html', context={'form': form})
    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(title = form.cleaned_data["title"], body = form.cleaned_data["body"], slug = form.cleaned_data["slug"])
            return redirect('/')
        else:
            return render(request, 'post/create.html', context={'errors': form.errors})

class PostList(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'post/index.html', context={'posts': posts})

class PostDetail(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        tags = post.tag_set.all()
        comments = post.comment_set.all()
        form = CommentForm()
        return render(request, 'post/detail.html', context={'post': post, 'comments': comments, 'tags': tags, 'form': form})
    def post(self, request, slug):
        form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if form.is_valid():
            Comment.objects.create(body=form.cleaned_data['body'], post=post)
            return redirect('/' + slug)

class PostEdit(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        form = PostForm()
        return render(request, 'post/edit.html', context={'post': post, 'form': form})
    def post(self, request, slug):
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.filter(slug=slug).update(title = form.cleaned_data["title"], body = form.cleaned_data["body"], slug = form.cleaned_data["slug"])
            return redirect('/')
        else:
            post = Post.objects.get(slug=slug)
            return render(request, 'post/edit.html', context={'post': post, 'errors': form.errors})

class PostDelete(View):
    def get(self, request, slug):
        Post.objects.filter(slug=slug).delete()
        return redirect('/')

class TagDetail(View):
    def get(self, request, name):
        tag = Tag.objects.get(name=name)
        return render(request, 'tag/detail.html', context={'tag': tag})

class TagCreate(View):
    def get(self, request):
        form = TagForm()
        posts = Post.objects.all()
        return render(request, 'tag/create.html', context={'form': form, 'posts': posts})
    def post(self, request):
        form = TagForm(request.POST)
        posts = Post.objects.all()
        if form.is_valid():
            Tag.objects.create(name = form.cleaned_data["name"])
            return redirect('/')
        else:
            return render(request, 'tag/create.html', context={'errors': form.errors, 'posts': posts})

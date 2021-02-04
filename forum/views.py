from django.shortcuts import render
from forum.models import Post, Comment
from .forms import CommentForm

def forum_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts":posts,
    }
    return render(request, "forum_index.html", context)

def forum_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by('-created_on')

    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "forum_category.html", context)

def forum_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data["author"],
                body = form.cleaned_data["body"],
                post = post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "forum_detail.html", context)
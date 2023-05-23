from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Post
from .forms import postForm
from django.contrib.auth.decorators import login_required
from accounts.models import Account, User
from django.contrib import messages
from .forms import postForm, postEditForm
from comments.models import Comment
from likes.models import Like
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from notifications.models import Notification
import os
from main.utils import uploadToGoogleDrive






@login_required
def like_view(request, slug):
    if request.method == "POST":
        post = Post.objects.get(slug=slug)
        account = Account.objects.get(user=request.user)
        qs = Like.objects.filter(post=post).filter(account=account)
        if not qs.exists():
            like = Like()
            like.account = account
            like.post = post
            like.save()
            post.likes += 1
            post.save()
            if like.account != post.account:
                notf = Notification()
                notf.account = post.account
                notf.post = post
                content = like.account.user.first_name + ' ' + like.account.user.last_name + ' liked  your post.'
                notf.content = content
                notf.save()
        else:
            like = Like.objects.get(post=post, account=account)
            like.delete()
            post.likes -= 1
            post.save()
        return HttpResponseRedirect(post.get_absolute_url)
    return HttpResponseRedirect('/posts/')

@login_required
def delete_view(request, slug):
    template_name = 'posts/confirm-delete.html'
    try:
        post = Post.objects.get(slug=slug)
    except:
        return redirect('/posts/')

    if post.account.user != request.user:
        messages.warning(request, "You are not authorized to perform the action.")
        return HttpResponseRedirect('/posts/')

    if request.method == 'POST':
        if request.POST.get('response') == 'yes':
            post.delete()
            messages.success(request, 'Post has been deleted successfully.')
            return HttpResponseRedirect('/posts/')
        else:
            messages.success(request, "Something went wrong. Couldn't delete the post")
            return HttpResponseRedirect(post.get_absolute_url)
    contex = {
        'post': post,
    }
    return render(request, template_name, contex)



@login_required
def edit_view(request, slug):
    template_name = 'posts/edit.html'
    try:
        post = Post.objects.get(slug=slug)
    except:
        return HttpResponseRedirect('/posts/')

    if post.account.user != request.user:
        messages.warning(request, "You are not authorized to perform the action.")
        return HttpResponseRedirect('/posts/')
    form = postEditForm(post, request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            post.content = form.cleaned_data.get('content')
            post.save()
            messages.success(request, 'Post has been updated successfully.')
            return HttpResponseRedirect(post.get_edit_url)
    contex = {
        'form': form,
        'post': post
    }
    return render(request, template_name, contex)


def detail_view(request, slug):
    template_name = 'posts/detail.html'
    account = None
    if request.user.is_authenticated:
        account = Account.objects.get(user=request.user)
    try:
        post     = Post.objects.get(slug=slug)
        comments = Comment.objects.all().filter(post=post).filter(parent__isnull=True)
        likes    = Like.objects.all().filter(post=post)
    except:
        return redirect('/posts/')
    posts = Post.objects.all().filter(is_active=True)

    liked = False
    for like in likes:
        if account == like.account:
            liked = True
    contex = {
        'post': post,
        'posts': posts,
        'comments': comments,
        'likes': likes,
        'liked': liked
    }
    return render(request, template_name, contex)

def postList_view(request):
    post_list = Post.objects.all().filter(is_active=True)
    paginator = Paginator(post_list, 5)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    template_name = 'posts/blog.html'
    contex = {
        'posts': posts,
        'form': postForm(),
        'comments': Comment.objects.all().filter(is_active=True)
    }
    return render(request, template_name, contex)

@login_required
def createPost_view(request):
    template_name = 'posts/create.html'
    form = postForm(request.POST or None, request.FILES or None, auto_id=False)
    if request.method == "POST":
        if form.is_valid():
            photo1 = form.cleaned_data.get('photo1')
            photo2 = form.cleaned_data.get('photo2')
            photo3 = form.cleaned_data.get('photo3')
            post = Post()
            post.account = Account.objects.get(user=request.user)
            post.content = form.cleaned_data.get('content')
            if photo1 != '' and photo1 != None:
                post.photo1 = photo1
            if photo2 != '' and photo2 != None:
                post.photo2 = photo2
            if photo3 != '' and photo3 != None:
                post.photo3 = photo3
            post.save()
            
            # uploading photo1
            if post.photo1 and os.path.exists(post.photo1.path):
                drive_id = uploadToGoogleDrive(post.photo1.path, 'POST')
            if drive_id != "":
                post.drive_photo1_link = "https://drive.google.com/thumbnail?id=" + str(drive_id)

            # uploading photo2
            if post.photo2 and os.path.exists(post.photo2.path):
                drive_id = uploadToGoogleDrive(post.photo2.path, 'POST')
            if drive_id != "":
                post.drive_photo2_ink = "https://drive.google.com/thumbnail?id=" + str(drive_id)

            # uploading photo3
            if post.photo3 and os.path.exists(post.photo3.path):
                drive_id = uploadToGoogleDrive(post.photo3.path, 'POST')
            if drive_id != "":
                post.drive_photo3_link = "https://drive.google.com/thumbnail?id=" + str(drive_id)
            post.save()



            messages.success(request, 'Your post has been uploaded successfully.')
            return HttpResponseRedirect(post.get_absolute_url)
    contex = {
        'form': form
    }
    return render(request, template_name, contex)
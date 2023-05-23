from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from accounts.models import Account
from comments.models import Comment
from django.http import HttpResponse
from django.contrib import messages
from posts.models import Post
from .forms import commentEditForm
from notifications.models import Notification


@login_required
def delete_view(request, slug):
	template_name = 'comments/confirm-delete.html'
	try:
		comment = Comment.objects.get(slug=slug)
	except:
		return HttpResponseRedirect('/posts/')
	if request.user != comment.account.user:
		messages.warning(request, "You are not authorized to perform the action.")
		return HttpResponseRedirect(comment.post.get_absolute_url)

	if request.method == 'POST':
		if request.POST.get('response') == 'yes':
			post = comment.post
			comment.delete()
			post.comments -= 1
			post.save()
			messages.success(request, 'Comment has been deleted successfully.')
			return HttpResponseRedirect(comment.post.get_absolute_url)
		else:
			messages.success(request, "Something went wrong. Couldn't delete the post")
			return HttpResponseRedirect(comment.post.get_absolute_url)
	contex = {
	    'post': comment.post,
	    'comment': comment
	}
	return render(request, template_name, contex)



@login_required
def edit_view(request, slug):
	template_name = 'comments/edit.html'
	try:
		comment = Comment.objects.get(slug=slug)
	except:
		return HttpResponseRedirect('/posts/')

	if comment.account.user != request.user:
		messages.warning(request, 'You are not authorized to perform the action.')
		return HttpResponseRedirect('/posts/')

	form = commentEditForm(comment, request.POST or None)
	if request.method == 'POST':
	    if form.is_valid():
	        comment.content = form.cleaned_data.get('content')
	        comment.save()
	        messages.success(request, 'Comment has been updated successfully.')
	        return HttpResponseRedirect(comment.get_edit_url)
	contex = {
	    'form': form,
	    'post': comment.post
	}
	return render(request, template_name, contex)








@login_required
def create_view(request):
	if request.method == "POST":
		try:
			post    = Post.objects.get(slug=request.POST.get('slug'))
			account = Account.objects.get(user=request.user)
			content = request.POST.get('comment')
		except:
			return HttpResponseRedirect('/posts/')
		comment = Comment()
		comment.account = account
		comment.post    = post
		comment.content = content
		comment.save()
		post.comments += 1
		post.save()

		# notify the owner of the post
		if post.account != comment.account:
			notf = Notification()
			notf.account = post.account
			notf.post = post
			content = comment.account.user.first_name + ' ' + comment.account.user.last_name + ' commented on your post "' + comment.content[:20] + '"'
			notf.content = content
			notf.save()
		commented_all = Comment.objects.all().filter(post=post)
		marked = []
		# notify others who also commented
		for commented in commented_all:
			if commented.account.user.email not in marked:
				if comment.account != post.account and comment.account != commented.account and commented.account != post.account:
					notf = Notification()
					notf.account = commented.account
					notf.post = post
					content = comment.account.user.first_name + ' ' + comment.account.user.last_name + ' also commented '+ post.account.user.first_name + "'s post " + '"' + comment.content[:20] + '"'
					notf.content = content
					notf.save()
					marked.append(commented.account.user.email)
		return HttpResponseRedirect(post.get_absolute_url)
	return HttpResponseRedirect('/posts/')






@login_required
def replyCreate_view(request):
	if request.method == "POST":
		parent_obj = None
		try:
			account   = Account.objects.get(user=request.user)
			parent_id = int(request.POST.get('parent_id'))
			content   = request.POST.get('reply')
			post      = Post.objects.get(slug=request.POST.get('post_slug'))
		except:
			parent_id = None

		if parent_id:
			parent_obj = Comment.objects.get(id=parent_id)
			if parent_obj:
				reply_comment = Comment()
				reply_comment.account = account
				reply_comment.post    = post
				reply_comment.content = content
				reply_comment.parent  = parent_obj
				reply_comment.save()
				post.comments += 1
				post.save()
				# notify to the comment owner
				if parent_obj.account != reply_comment.account:
					content = reply_comment.account.user.first_name + ' ' + reply_comment.account.user.last_name  + ' replied to your comment "' + reply_comment.content[:20] + '"'
					notf = Notification()
					notf.account = parent_obj.account
					notf.post    = post
					notf.content = content
					notf.save()

				# notify others who also replied to the comment avoiding repeatation...
				marked  = []
				replies = parent_obj.replies.all()
				for replied in replies:
					if replied.account.user.email not in marked:
						if reply_comment.account != replied.account and parent_obj.account != replied.account: # don't notify the replier him/her-self
							content = reply_comment.account.user.first_name + ' ' + reply_comment.account.user.last_name  + ' also replied on ' + parent_obj.account.user.first_name + "'s comment " + '"' + reply_comment.content[:20] + '"'	
							notf = Notification()
							notf.account = replied.account
							notf.post    = post
							notf.content = content
							notf.save()
							marked.append(replied.account.user.email)	
		return HttpResponseRedirect(post.get_absolute_url)
	return HttpResponseRedirect('/posts/')
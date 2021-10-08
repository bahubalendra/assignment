from django.shortcuts import render, redirect
from django.http import Http404, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, SubComment
from django.db.models import Q


@login_required
def search(request):
	q = request.GET.get('q')
	if q:
		users = User.objects.filter(
		Q(username__icontains = q) |
		Q(comment__icontains = q)
		).distinct()
	else:
		users = request.user.profile.non_followed_user
	return render(request, 'search.html', {'users': users})

@login_required
def home(request):
	if request.method == "POST":
		text = request.POST.get('text')
		img = request.FILES.get('post_image')
		post = Post(user = request.user, text = text, picture=img)
		post.save()
		return redirect('home')

	following_users = list(request.user.profile.following.all())
	following_users.append(request.user)
	posts = Post.objects.filter(user__in = following_users).order_by('-created_at')
	parms = {
		'non_followed_user': request.user.profile.non_followed_user,
		'posts': posts,
	}
	return render(request, 'home.html', parms)


@login_required
def add_comment(request):
	if request.method =="POST":
		post_id = request.POST.get('post_id')
		comm = request.POST.get('comm')
		obj = Comment.objects.create(user=request.user, 
			post = Post.objects.get(id=int(post_id)),
			comm = comm,
			)
		return JsonResponse({
			'url': request.user.profile.profile_pic.url,
			'name': f"{request.user.first_name} {request.user.last_name}",
			'text': obj.comm,
			'id': obj.id,
			})
	raise Http404()

@login_required
def add_subcomment(request):
	if request.method =="POST":
		comm_id = request.POST.get('comm_id')
		comm = request.POST.get('comm')
		obj = SubComment.objects.create(user=request.user, 
			comment = Comment.objects.get(id=int(comm_id)),
			comm = comm,
			)
		return JsonResponse({
			'url': request.user.profile.profile_pic.url,
			'name': f"{request.user.first_name} {request.user.last_name}",
			'text': obj.comm,
			'id': obj.id,
			})
	raise Http404()






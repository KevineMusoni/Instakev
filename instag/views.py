from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile,Post,Likes,Follows,Saves,Comment
from django.contrib.auth.models import User
from .forms import PostForm,CommentForm,ProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/accounts/login/')
def home(request):
    image_form = PostForm()
    images = Post.objects.all()
    commentform = CommentForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            request.user.profile.post(form)
    return render(request, 'index.html', locals())


@login_required(login_url='/accounts/login/')
def mine(request):
    images = request.user.profile.posts.all()
    user_object = request.user
    user_images = user_object.profile.posts.all()
    return render(request, 'myprofile.html', locals())


@login_required(login_url='/accounts/login/')
def edit(request):
    if request.method == 'POST':
        print(request.FILES)
        new_profile = ProfileForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if new_profile.is_valid():
            new_profile.save()
            print(new_profile.fields)
            return redirect('myaccount')
    else:
        new_profile = ProfileForm(instance=request.user.profile)
    return render(request, 'edit.html', locals())


@login_required(login_url='/accounts/login/')
def user(request, user_id):
    user_object=get_object_or_404(User, pk=user_id)
    if request.user == user_object:
        return redirect('myaccount')
    isfollowing = user_object.profile not in request.user.profile.follows
    user_images = user_object.profile.posts.all()
    return render(request, 'profile.html', locals())


@login_required(login_url='/accounts/login/')
def comment_on(request, post_id):
    commentform = CommentForm()
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user.profile
            comment.photo = post
            comment.save()
    return render(request, 'posts.html', locals())


@login_required(login_url='/accounts/login/')
def like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    request.user.profile.like(post)
    return JsonResponse(post.count_likes, safe=False)

@login_required(login_url='/accounts/login/')
def save(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    request.user.profile.save_image(post)
    return JsonResponse({}, safe=False)


@login_required(login_url='/accounts/login/')
def unlike(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    request.user.profile.unlike(post)
    return JsonResponse(post.count_likes, safe=False)

@login_required(login_url='/accounts/login/')
def togglefollow(request, user_id):
    target = get_object_or_404(User, pk=user_id).profile
    request.user.profile.togglefollow(target)
    response = [target.followers.count(),target.following.count()]
    return JsonResponse(response, safe=False)

@login_required(login_url='/accounts/login/')
def find(request, name):
    results = Profile.find_profile(name)
    return render(request, 'searchresults.html', locals())


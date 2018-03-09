from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime as dt 
from django.contrib.auth.decorators import login_required
from .models import Profile,Post,Comments,Likes,Follow
from . forms import NewPostForm, NewCommentForm,NewProfileForm
import mimetypes
from django.contrib.auth.models import User
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def index(request):
    current_user = request.user
    grammy = Post.all_images()
    profiles = Profile.get_profile()
    comment = Comments.get_comments()
    like = Likes.get_likes()
    following = Follow.get_following()
    following_posts = []

    for follow in following:
        for posts in post:
            if follow.profile == post.profile:
                following_posts.append(post)
    return render(request,'index.html',{"grammy":grammy,"profiles":profiles,"following": following, "user":current_user, "following_posts":following_posts,"like":like})

#logged in user on the profile icon

@login_required(login_url='/accounts/register')
def profile(request,id):
    current_user = request.user
    single_profile = Profile.objects.get(id = id)
    grammy = Post.all-images()
    return render(request, 'all-grammy/my_profile.html', {"current_user":current_user,"grammy":grammy,"single_profile":single_profile})
    

#displaying the posts page of a looged in user
@login_required(login_url='/accounts/register')
def all_images(request):
    current_user = request.user
    posts = Post.get_posts()
    following_posts = []
    for follow in following:
        for post in posts :
            if follow.profile == post.profile:
                following_posts.append(post)

    return render(request, 'all-grammy/posts.html',{"following":following, "user":user, "following_posts":following_posts})            

#adding a profile to the posts
@login_required(login_url='/accounts/register')
def follow(request,id):
    current_user = request.user
    follow_profile = Profile.objects.get(id=id)
    following = Follow(user = current_user,profile = follow_profile)
    following.save()

    return redirect("following")
    context = {
        "follow":follow_profile,
        "following":following
    }
    return render(request,'index.html', context)



#adding a like to a post
@login_required(login_url='/accounts/register')
def likes(redirect,id):
    current_user = request.user
    current_post = Post.objects.get(id=id)
    likes = Likes(user = current_user,post = current_post,likes_number = 1)
    likes.save()
    return redirect(post,current_post.id)

# displaying a single post
@login_required(login_url='/accounts/register')
def post(request,id):
    current_post = request.user
    try:
        current_post = Post.objects.get(id=id)
        likes = Like.num_likes(id)
        like = Likes.get_likes(filter(post = id).filter(user = current_user))
    except DoesNotExist:
        raise Http404()
    return render(request, 'all-grammy/posts.html',{"post":current_post,"likes":likes,"like":like})        


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            posts = form.save(commit=False)
            posts.save()
            return redirect('/')
    else:
        form = NewPostForm()
    return render(request, 'all-grammy/new-post.html', {"form":form})     


@login_required(login_url='/accounts/register')
def comment(request):
    post = Post.objects.all()
    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('/')
    else:
        form = NewCommentForm()
    return render(request,'all-grammy/new-comment.html', {"form":form,"current_post":post})        

@login_required(login_url='/accounts/register')
def profile(request):
    post = Post.objects.all()
    if request.method == 'POST':
        form = NewProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('/')
    else:
        form = NewProfileForm()
    return render(request,'all-grammy/new-profile.html', {"form":form,"current_post":post})


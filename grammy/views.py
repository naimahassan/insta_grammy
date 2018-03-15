from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime as dt 
import mimetypes
from django.contrib.auth.decorators import login_required
from .models import Profile,Post,Comment,Likes,Follow
from . forms import NewPostForm, NewCommentForm,NewProfileForm,NewFollowForm
from django.contrib.auth.models import User
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
import os


# Create your views here.

@login_required(login_url='/accounts/login')
def index(request):
    # current_user = request.user
    grammy = Post.all_images()
    # profiles = Profile.get_profile()
    comment_form = NewCommentForm
    profile_form = NewProfileForm
    comments = Comment.get_comments()
    follows = NewFollowForm
    # like = Likes.get_likes()
    # following = Follow.get_following()
    # grammy = []
    # for followed in following:
    #     profiles = Profile.objects.filter(id=followed.profile.id)
    #     # fro profile in profiles:
    #     post = Post.objects.filter(user=profile.user)
    #     for image in post:
    #         grammy.append(image)
    return render(request,'index.html',{"grammy":grammy,"comment_form":NewCommentForm,"profile_form":NewProfileForm ,"NewFollowForm":follow ,"comments":comments})

#logged in user on the profile icon

@login_required(login_url='/accounts/register')
def profile(request,user_id):
    current_user = request.user
    
    grammy = Post.objects.filter(profile__id=user_id)
    post_profile=Post.objects.get(id=user_id)

    return render(request, 'all-grammy/my-profile.html', {"current_user":current_user,"grammy":grammy,"post_profile":post_profile})
    
@login_required(login_url='/accounts/register')
def search_profile(request):
    if 'user_name' in request.GET and request.GET["user_name"]:
       search_term = request.GET.get('user_name')
       searched_user = Profile.searched_profile(search_term)

       message = f"{search_term}"

       return render(request, 'all-grammy/search.html',{"message":message,"profiles": searched_user})

    else:
       message = "You haven't searched for any term"
       return render(request, 'all-grammy/search.html',{"message":message})



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
def follow(request):
    form = NewFollowForm(request.POST)
    if form.is_valid():
        follow = form.instance
        follow.user = request.user
        follow.save()
        return redirect('/')
# def follow(request,id):
#     current_user = request.user
#     follow_profile = Profile.objects.get(id=id)
#     following = Follow(user = current_user,profile = follow_profile)
#     following.save()

#     return redirect("following")
#     context = {
#         "follow":follow_profile,
#         "following":following
#     }
#     return render(request,'index.html', context)



#adding a like to a post
@login_required(login_url='/accounts/register')
def likes(redirect,id):
    current_user = request.user
    current_post = Post.objects.get(id=id)
    likes = Likes(user = current_user,post = current_post,likes_number = 1)
    likes.save()
    return redirect(post,current_post.id)


@login_required(login_url='/accounts/login')
def single_image(request, photo_id):
    '''
    View funtion to display a particular image with its details
    '''
    image = Post.objects.get(id =id)
    user_info = Profile.objects.get(user=image.user.id)#fetch the profile of the user who posted
    comments = Comment.objects.filter(post=image.id)
    validate_vote = Likes.objects.filter(user=request.user,post=photo_id).count()
    upvotes = Likes.get_post_likes(image.id)
    likes = len(upvotes)
    return render(request, 'all-grammy/posts.html', {'image':image, "user_info":user_info,"comments":comments, "likes":likes, "validate_vote":validate_vote})


#displaying a single post
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
            post = form.save(commit=False)
            post = current_user
            post.save()
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
def new_profile(request):
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

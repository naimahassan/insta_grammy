from django.db import models
from tinymce.models import HTMLField
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
# Creating Image models. 

# profile model
class Profile(models.Model):
     image = models.ImageField(upload_to = 'profile/', null = True, blank = True)
     bio = models.CharField(max_length = 255,blank = True)
     user = models.ForeignKey(User, on_delete=models.CASCADE)
    

     def __str__(self):
        return str(self.image)
            
     def save_profile(self):
        self.save()

     def delete_profile(self):
        self.delete() 

     @classmethod
     def get_profile(cls):
        profiles = Profile.objects.all()
        return profiles


     @classmethod
     def searched_profile(cls,search_term):
        query = cls.objects.filter(bio__icontains=search_term)
        return query    

                  




class Follow(models.Model):
    # user = models.ForeignKey(User)
    profile = models.ForeignKey(Profile,null = True)
    
    def __str__(self):
        return self.profile

    @classmethod
    def get_following(cls,user_id):
        following =  Follow.objects.filter(user=user_id).all()
        return following





# post models
class Post(models.Model):
    image = models.ImageField(upload_to = 'post/', null = False, blank = False, default=1)     
    name = models.CharField(max_length = 60)
    caption = HTMLField()
    profile = models.ForeignKey(Profile, null = True)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.name

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def all_images(cls):
        grammy = cls.objects.all() 
        return grammy

    @classmethod
    def get_profile_posts(cls,profile_id):
        profile_posts = Post.objects.filter(profile = profile_id).all()
        return profile_posts
class Likes(models.Model):
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    likes_number = models.PositiveIntegerField(null=True, blank=True)

    def __int__(self):
        return self.likes
    
    #one post like
    @classmethod
    def get_likes(cls):
        likes = Likes.objects.all()
        return likes  

    #total numbers of likes
    @classmethod
    def num_likes(cls,post_id):
        post = Likes.objects.filter(post=post_id)  
        return post 


class Comment(models.Model):
    comments = models.TextField(max_length = 100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.comments


    # @classmethod
    def get_comments(cls,post_id):
        comment =  Comment.objects.all()
        return comment    
    
    #to get comments on a single post
    def get_post_comments(self,post_id):
        comments_list = Comment.objects.filter(id=post_id)
        return comments_list



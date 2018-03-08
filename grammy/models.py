from django.db import models
from tinymce.models import HTMLField
from django.core.urlresolvers import reverse
# Creating Image models. 

# user models
class User(models.Model):
    first_name = models.CharField(max_length = 60)
    last_name = models.CharField(max_length = 60)
    email = models.EmailField()
    image = models.ImageField(upload_to = 'user/',default=1)

    def __str__(self):
        return self.first_name

    def save_user(self):
        self.save()    
 
    
    @classmethod
    def image_profile(cls):
        gram= cls.objects.all()
        return gram


# profile model
class Profile(models.Model):

     image = models.ImageField(upload_to = 'user/', null = True, blank = True)
     bio = models.CharField(max_length = 255,blank = True)
     user =  models.ForeignKey(User, null = True, db_column="image_id", to_field='id')

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

    #  def get_other_profile(cls,user_id):
    #     profiles = Profile.objects.all()
    #     other_profiles = []
    #     for profile in profiles:
    #         if profile.user.id != user_id:
    #     return other_profiles                   

class Comments(models.Model):
    comments = models.TextField(max_length = 100)
    user = models.ForeignKey(User,null = True)


    def __str__(self):
        return self.comments


    @classmethod
    def get_comments(cls):
        comment =  Follow.objects.all()
        return comment    



class Follow(models.Model):
    user = models.ForeignKey(User,null = True)
    profile = models.ForeignKey(Profile,null = True)
    
    def __str__(self):
        return self.user.first_name

    @classmethod
    def get_following(cls):
        following =  Follow.objects.all()
        return following


class Likes(models.Model):
    likes = models.IntegerField(default=0)
    user =  models.ForeignKey(User, null = True)
    likes_number = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.likes

    @classmethod
    def get_post_likes(cls,post_id):
        post_likes = Likes.objects.filter(post = post_id)
        return post_likes  


# post models
class Post(models.Model):
    image = models.ImageField(upload_to = 'user/', null = False, blank = False, default=1)     
    name = models.CharField(max_length = 60)
    caption = HTMLField()
    user = models.ForeignKey(User, null = True)
    likes = models.IntegerField(default=0)
    profile = models.ForeignKey(Profile, null = True)
    comments = models.ForeignKey(Comments, null = True)
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
 



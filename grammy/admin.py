from django.contrib import admin
from .models import Post,Profile,User,Likes,Comments

# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(User)
admin.site.register(Likes)
admin.site.register(Comments)

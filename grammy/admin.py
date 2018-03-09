from django.contrib import admin
from .models import Post,Profile,Likes,Comments

# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Likes)
admin.site.register(Comments)

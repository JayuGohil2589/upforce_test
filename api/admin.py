from django.contrib import admin
from api.models import Blog, Blogslike

# Register your models here.
admin.site.register(Blog, admin.ModelAdmin)
admin.site.register(Blogslike, admin.ModelAdmin)

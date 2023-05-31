from django.contrib import admin
from api.models import User, Blog, Blogslike

# Register your models here.
admin.site.register(User, admin.ModelAdmin)
admin.site.register(Blog, admin.ModelAdmin)
admin.site.register(Blogslike, admin.ModelAdmin)

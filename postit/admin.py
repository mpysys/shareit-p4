from django.contrib import admin

# Register your models here.
from .models import Postit, PostLike


class PostLikeAdmin(admin.TabularInline):
    model = PostLike

class PostAdmin(admin.ModelAdmin):
    inlines = [PostLikeAdmin]
    list_display = ['__str__', 'user']
    class Meta:
        model = Postit
admin.site.register(Postit, PostAdmin)

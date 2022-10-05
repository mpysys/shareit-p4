from django.contrib import admin

# Register your models here.
from .models import Postit

class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user']
    class Meta:
        model = Postit
admin.site.register(Postit, PostAdmin)

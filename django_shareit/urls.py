"""django_shareit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

from postit.views import (
    homepage_view,
    postit_actions_view,
    postit_delete_view,
    postit_detail_view,
    postit_list_view,
    post_create_view,

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_view),
    path('create-post', post_create_view),
    path('postit/', postit_list_view),
    path('postit/<int:postit_id>', postit_detail_view),
    path('api/postit/', include('postit.urls'))

]

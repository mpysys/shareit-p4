from django.urls import path

from .views import (
    homepage_view,
    postit_actions_view,
    postit_delete_view,
    postit_detail_view,
    postit_list_view,
    post_create_view,

)

urlpatterns = [
    path('', postit_list_view),
    path('action/', postit_actions_view),
    path('create/', post_create_view),
    path('<int:postit_id>/', postit_detail_view),
    path('<int:postit_id>/delete/', postit_delete_view),

]

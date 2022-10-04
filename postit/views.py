from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
import random

from .forms import PostForm
from .models import Postit

# Create your views here.


def homepage_view(request, *args, **kwargs):
    return render(request, 'pages/home.html', context={}, status=200)

# create a new post and add to database


def post_create_view(request, *args, **kwargs):
    form = PostForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = PostForm()
    return render(request, 'comp/form.html', context={"form": form})


def postit_list_view(request, *args, **kwargs):
    """
    REST API VIEW
    return json data
    """
    query_set = Postit.objects.all()
    post_list = [{"id": x.id, "content": x.content,
                 "likes": random.randint(0, 150)} for x in query_set]
    data = {
        "isUser": False,
        "response": post_list
    }
    return JsonResponse(data)


def postit_detail_view(request, postit_id, *args, **kwargs):
    """
    REST API VIEW
    return json data
    """
    data = {
        "id": postit_id,
    }
    status = 200
    try:
        obj = Postit.objects.get(id=postit_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not found"
        status = 404
    return JsonResponse(data, status=status)
    # json.dumps content_type='application/json'

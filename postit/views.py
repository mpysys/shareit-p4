from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
import random
from django.conf import settings
from django.utils.http import url_has_allowed_host_and_scheme

from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .forms import PostForm
from .models import Postit
from .serializers import PostSerializer, PostActionSerializer
# Create your views here.


def homepage_view(request, *args, **kwargs):
    return render(request, 'pages/home.html', context={}, status=200)

# create a new post and add to database
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_create_view(request, *args, **kwargs):
    serializer = PostSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)


@api_view(['GET'])
def postit_list_view(request, *args, **kwargs):
    query_set = Postit.objects.all()
    serializer = PostSerializer(query_set, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def postit_detail_view(request, postit_id, *args, **kwargs):
    query_set = Postit.objects.filter(id=postit_id)
    if not query_set.exists():
        return Response({}, status=404)
    obj = query_set.first()
    serializer = PostSerializer(obj)
    return Response(serializer.data, status=200)


@api_view(['DELETE', 'POST'])
@permission_classes([IsAuthenticated])
def postit_delete_view(request, postit_id, *args, **kwargs):
    query_set = Postit.objects.filter(id=postit_id)
    if not query_set.exists():
        return Response({}, status=404)
    query_set = query_set.filter(user=request.user)
    if not query_set.exists():
        return Response({"message": "You cannot delete this post"}, status=401)
    obj = query_set.first()
    obj.delete()
    return Response({"message": "The post has been deleted"}, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def postit_actions_view(request, *args, **kwargs):
    """
    User can take the following actions: like, unlike, share
    id is required
    """
    serializer = PostActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        postit_id = data.get("id")
        action = data.get("action")

        query_set = Postit.objects.filter(id=postit_id)
        if not query_set.exists():
            return Response({}, status=404)
        obj = query_set.first()
        if action == "like":
            obj.likes.add(request.user)
            serializer = PostSerializer(obj)
            return Response(serializer.data, status=200)
        elif action == "unlike":
            obj.likes.remove(request.user)
        elif action == "share":
            # will incorporate later // to do
            pass 
    return Response({}, status=200)


# OLD CODE
def post_create_view_og_django(request, *args, **kwargs):
    user = request.user
    if not request.user.is_authenticated:
        user = None
        if request.headers.get('X-Requested-With' or
                               "HTTP_X_REQUESTED_WITH") == 'XMLHttpRequest':
            return JsonResponse({}, status=401)
        return redirect(settings.LOGIN_URL)
    form = PostForm(request.POST or None)
    next_url = request.POST.get('next') or None  # pass next_url to respones
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = user
        obj.save()
        if request.headers.get('X-Requested-With' or
                               "HTTP_X_REQUESTED_WITH") == 'XMLHttpRequest':
            return JsonResponse(obj.serialize(),
                                status=201)  # testing if ajax is true
        if next_url is not None and url_has_allowed_host_and_scheme(next_url, 'localhost'):
            # if next_url invalid, no redirect - and check if safe
            return redirect(next_url)
        form = PostForm()
    if form.errors:
        if request.headers.get('X-Requested-With' or
                               "HTTP_X_REQUESTED_WITH") == 'XMLHttpRequest':
            return JsonResponse(form.errors, status=400)
    return render(request, 'comp/form.html', context={"form": form})


def postit_list_view_og_django(request, *args, **kwargs):
    """
    REST API VIEW
    return json data
    """
    query_set = Postit.objects.all()
    post_list = [x.serialize() for x in query_set]
    data = {
        "isUser": False,
        "response": post_list
    }
    return JsonResponse(data)


def postit_detail_view_og_django(request, postit_id, *args, **kwargs):
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

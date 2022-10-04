from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import Postit

# Create your views here.


def homepage_view(request, *args, **kwargs):
    return render(request, 'pages/home.html', context={}, status=200)


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

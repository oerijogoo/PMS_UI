from django.shortcuts import render

import requests
from django.http import JsonResponse, HttpResponse
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def api_view(request):
    api_url = "https://localhost:44308/api/goodsReceivedNote/instocks"
    response = requests.get(api_url, verify=False)
    if response.status_code == 200:
        data = response.json()
        # process the data here
        return render(request, 'graph.html', {'data': data})
    else:
        # handle the error here
        return HttpResponse('Error: {}'.format(response.status_code))


def index(request):
    return HttpResponse('welcome here')


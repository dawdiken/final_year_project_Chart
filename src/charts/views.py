from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response




class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {"customer": 10})


def get_data(request, *args, **kwargs):
    data = {
        "sale": 100,
        "customers": 10,
    }
    return JsonResponse(data)

class ChartData(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = ["Des", "Mike", "Michelle", "Paul", "Brian", "Niall"]
        default_items = [10,15,17,25,9,7]
        data = {
            "labels": labels,
            "default": default_items,

        }
        return Response(data)
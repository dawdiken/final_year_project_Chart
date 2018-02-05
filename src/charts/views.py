from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse ,request
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from django.shortcuts import redirect
# from django.db.backends import mysql
#import MySQLdb
import pymysql
import json
from django.http import HttpResponse


class Data_users(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        return render(request, 'charts.html', {"customer": 10})


def get_data(request, *args, **kwargs):
    data = {
        "sale": 100,
        "customers": 10,
    }
    return JsonResponse(data)


def homeView(request):
    return render(request, "landing_page.html")


class ChartUsers(APIView):
    """
    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # login_url = '/login/'
    # redirect_field_name = 'redirect_to'
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        conn = pymysql.connect(host="35.184.175.243",  # your host, usually localhost
                               user="root",  # your username
                               passwd="test12",  # your password
                               db="engineering")  # name of the data base
        try:
            cursor = conn.cursor()
            cursor.execute("select userName from users")
            rows = cursor.fetchall()
            jsonliststuff = json.dumps(rows)
            print(jsonliststuff)
            labels = []
            print(rows)
            for line in rows:
                print(line)
                for element in line:
                    print(element)
                    # labels.add()

            # print(labels.all)
        finally:
            conn.close()

        labels = [["Des"], ["Mike"], ["Michelle"], ["Paul"], ["Brian"], ["Niall"]]
        print(labels)
        default_items = [10, 15, 17, 25, 9, 7]
        data = {
            "labels": rows,
            "default": default_items,

        }
        return Response(data)


from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')
from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
# from django.db.backends import mysql
#import MySQLdb
import pymysql
import json
from django.http import HttpResponse



class Data_users(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {"customer": 10})


def get_data(request, *args, **kwargs):
    data = {
        "sale": 100,
        "customers": 10,
    }
    return JsonResponse(data)

def homeView(request):
    return render(request, "landing_page.html")



# def homeView(request, *args, **kwargs):
#     data = {
#         "sale": 100,
#         "customers": 10,
#     }
#     return JsonResponse(data)

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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
#
#
# def show_color(request):
#     print (request)
#     if "favorite_color" in request.COOKIES:
#         return HttpResponse("Your favorite color is %s" % \
#             request.COOKIES["favorite_color"])
#     else:
#         return HttpResponse("You don't have a favorite color.")
#
#
# def set_color(request):
#     print(request)
#
#     if "/favorite_color" in request:
#         # Create an HttpResponse object...
#         response = HttpResponse("Your favorite color is now %s" % \
#             request["favorite_color"])
#
#         # ... and set a cookie on the response
#         response.set_cookie("favorite_color",
#                             request.GET["favorite_color"])
#
#         return response
#
#     else:
#         return HttpResponse("didnt work")
#
# from django.http import HttpResponse
# from django.shortcuts import render
#
# def login(request):
#     if request.method == 'POST':
#         if request.session.test_cookie_worked():
#             request.session.delete_test_cookie()
#             return HttpResponse("You're logged in.")
#         else:
#             return HttpResponse("Please enable cookies and try again.")
#     request.session.set_test_cookie()
#     return render(request, 'foo/login_form.html')
#
# def post_comment(request, new_comment):
#     if request.session.get('has_commented', False):
#         return HttpResponse("You've already commented.")
#     c = comments.Comment(comment=new_comment)
#     c.save()
#     request.session['has_commented'] = True
#     return HttpResponse('Thanks for your comment!')

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
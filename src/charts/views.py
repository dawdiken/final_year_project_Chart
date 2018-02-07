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
        if not request.user.email.endswith('@gmail.com'):
            return redirect('/permissionredirect')
        return render(request, 'charts.html', {"customer": 10})


def get_data(request, *args, **kwargs):
    data = {
        "sale": 100,
        "customers": 10,
    }
    return JsonResponse(data)


def permissionredirect(request, *args, **kwargs):

    return render(request, 'nopermission.html')


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


class usertable(View):
    def get(self, request, *args, **kwargs):
        # if not request.user.is_authenticated:
        #     return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        # if not request.user.email.endswith('@gmail.com'):
        #     return redirect('/permissionredirect')
        return render(request, 'usertable.html')


class displayUsers(APIView):
    """
    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # login_url = '/login/'
    # redirect_field_name = 'redirect_to'
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        try:
            cnx = pymysql.connect(host="35.184.175.243",  # your host, usually localhost
                               user="root",  # your username
                               passwd="test12",  # your password
                               db="engineering")  # name of the data base
            cursor = cnx.cursor()

            query = ("select * from users")

            query = ("SELECT userID, userName, pass FROM users ")


            cursor.execute(query)

            response = []
            # rows = cursor.fetchall()
            # for row in rows:
            #     for key, dict_list in row.iteritems():
            #         count = dict_list[1]
            #         year = dict_list[2]
            #         response.append({'userID': count['v'], 'userName': year['v']})
            #
            # print (json.dumps(response))
            # rows = cursor.fetchall()
            # print(cursor.fetchall())
            # print(rows.userName)
            # thisstuff = []
            results = cursor.fetchall()
            for row in results:
                userID = row[0]
                userName = row[1]
                passw = row[2]
                # Now print fetched result
                # print("fname={},lname={},passw={}".format(userID, userName, passw))
                response.append({'userID': userID, 'userName': userName})
            print("response json" + json.dumps(response))



            # for (userID, userName) in cursor:
            #     print("{}, {} ".format(
            #         userID, userName))

            # rows = cursor.fetchall()

            # print(rows)



            # cursor = conn.query()
            # query = ("SELECT first_name, last_name, hire_date FROM employees "
            #          "WHERE hire_date BETWEEN %s AND %s")
            # cursor.execute("select * from users")
            # rows = cursor.fetchall()
            # jsonliststuff = json.dumps(rows)
            # # print(jsonliststuff)
            # labels = []
            # print(rows)
            # print(rows.userName)

        finally:
            cursor.close()
            cnx.close()

        # labels = [["Des"], ["Mike"], ["Michelle"], ["Paul"], ["Brian"], ["Niall"]]
        # print(labels)
        # default_items = [10, 15, 17, 25, 9, 7]
        # data2 = json.dumps(response)
        # print (data2)
        # data = {
        #     "labels": rows,
        #     "default": default_items,
        #
        # }
        data2 = json.dumps(response)
        # print (data2)
        return JsonResponse(json.dumps(response), safe=False)

class worktable(View):
    def get(self, request, *args, **kwargs):
        # if not request.user.is_authenticated:
        #     return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        # if not request.user.email.endswith('@gmail.com'):
        #     return redirect('/permissionredirect')
        return render(request, 'worktable.html')

class workinfo(View):
    def get(self, request, *args, **kwargs):
        # if not request.user.is_authenticated:
        #     return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        # if not request.user.email.endswith('@gmail.com'):
        #     return redirect('/permissionredirect')
        return render(request, 'showjob.html')

class displayWork(APIView):
    """
    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # login_url = '/login/'
    # redirect_field_name = 'redirect_to'
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        try:
            cnx = pymysql.connect(host="35.184.175.243",  # your host, usually localhost
                               user="root",  # your username
                               passwd="test12",  # your password
                               db="engineering")  # name of the data base
            cursor = cnx.cursor()

            # query = ("select * from users")

            query = ("SELECT * FROM workon")


            cursor.execute(query)

            response = []

            results = cursor.fetchall()
            print(results)

            for row in results:
                jobID = row[0]
                jobNum = row[1]
                active = row[2]
                customer_ID = row[3]
                department_ID = row[4]
                partID = row[5]
                machineID = row[6]
                response.append({'jobID': jobID, 'jobNum': jobNum, 'active': active, 'customer_ID': customer_ID,
                                 'department_ID': department_ID, 'partID': partID, 'machineID': machineID})
            print("response json" + json.dumps(response))

        finally:
            cursor.close()
            cnx.close()

        data2 = json.dumps(response)
        # print (data2)
        return JsonResponse(json.dumps(response), safe=False)


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
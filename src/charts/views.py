from django.views.generic import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from django.shortcuts import redirect
import pymysql
import json
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


class Data_users(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        if request.user.email.endswith('@gmail.com'):
            return render(request, 'charts.html', {"customer": 10})
        elif request.user.email.endswith('@eng.com'):
            return render(request, 'charts.html', {"customer": 10})
        else:
            return redirect('/permissionredirect')


def get_data(request, *args, **kwargs):
    data = {
        "sale": 100,
        "customers": 10,
    }
    return JsonResponse(data)


def permissionredirect(request, *args, **kwargs):
    return render(request, 'nopermission.html')


def about(request, *args, **kwargs):
    return render(request, 'about.html')


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
        finally:
            conn.close()
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
            query = ("SELECT userID, userName, pass FROM users ")
            cursor.execute(query)
            results = cursor.fetchall()
            response = []
            for row in results:
                userID = row[0]
                userName = row[1]
                passw = row[2]
                response.append({'userID': userID, 'userName': userName})
        finally:
            cursor.close()
            cnx.close()
        return JsonResponse(json.dumps(response), safe=False)


class worktable(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        if request.user.email.endswith('@gmail.com'):
            return render(request, 'worktable.html')
        elif request.user.email.endswith('@eng.com'):
            return render(request, 'worktable.html')
        else:
            return redirect('/permissionredirect')


class changeWork(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        if request.user.email.endswith('@eng.com'):
            return render(request, 'changework.html')
        else:
            return redirect('/permissionredirect')


class allWorktable(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        if request.user.email.endswith('@gmail.com'):
            return render(request, 'allwork.html')
        elif request.user.email.endswith('@eng.com'):
            return render(request, 'allwork.html')
        else:
            return redirect('/permissionredirect')


class workinfo(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        if not request.user.email.endswith('@gmail.com'):
            return redirect('/permissionredirect')
        return render(request, 'showjob.html')


class displayAllWork(APIView):
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
            query = ("SELECT * FROM workon_copy")
            cursor.execute(query)
            results = cursor.fetchall()
            response = []
            for row in results:
                jobID = row[0]
                jobNum = row[1]
                active = row[2]
                customer_ID = row[3]
                department_ID = row[4]
                partID = row[5]
                batchNumber = row[6]
                qtyOrdered = row[7]
                machineID= row[8]
                qty_finished = row[9]
                qty_scrap = row[10]
                response.append({'jobID': jobID, 'jobNum': jobNum, 'active': active, 'customer_ID': customer_ID,
                                 'department_ID': department_ID, 'partID': partID, 'machineID': machineID, 'qty_finished': qty_finished, 'qty_scrap': qty_scrap, 'qtyOrdered': qtyOrdered})
        finally:
            cursor.close()
            cnx.close()
        return JsonResponse(json.dumps(response), safe=False)


class changeWorkInfo(View):
    """
    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # login_url = '/login/'
    # redirect_field_name = 'redirect_to'
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        if request.method == 'GET':
            jobnum = request.GET['jobnum']
            newQty = request.GET['newQty']
        try:
            cnx = pymysql.connect(host="35.184.175.243",  # your host, usually localhost
                               user="root",  # your username
                               passwd="test12",  # your password
                               db="engineering")  # name of the data base
            cursor = cnx.cursor()
            query = ("UPDATE workon_copy SET qty_ordered = %s WHERE jobID = %s")
            cursor.execute(query,(newQty,jobnum))
            cnx.commit()
            query = ("SELECT * FROM workon_copy WHERE jobID = %s")
            cursor.execute(query, jobnum)
            response = []
            results = cursor.fetchall()
            for row in results:
                jobID = row[0]
                jobNum = row[1]
                active = row[2]
                customer_ID = row[3]
                department_ID = row[4]
                partID = row[5]
                batchNumber = row[6]
                qtyOrdered = row[7]
                machineID= row[8]
                qty_finished = row[9]
                qty_scrap = row[10]
                response.append({'jobID': jobID, 'jobNum': jobNum, 'active': active, 'customer_ID': customer_ID,
                                 'department_ID': department_ID, 'partID': partID, 'machineID': machineID, 'qty_finished': qty_finished, 'qty_scrap': qty_scrap, 'qtyOrdered': qtyOrdered})
            print("response json" + json.dumps(response))
        finally:
            cursor.close()
            cnx.close()
        return JsonResponse(json.dumps(response), safe=False)


class deleteWorkInfo(APIView):
    """
    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # login_url = '/login/'
    # redirect_field_name = 'redirect_to'
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        if request.method == 'GET':
            jobnum = request.GET['jobnum']
        try:
            cnx = pymysql.connect(host="35.184.175.243",  # your host, usually localhost
                               user="root",  # your username
                               passwd="test12",  # your password
                               db="engineering")  # name of the data base
            cursor = cnx.cursor()
            query = ("DELETE FROM workon_copy WHERE jobID = %s")
            cursor.execute(query, (jobnum))
            cnx.commit()
        finally:
            cursor.close()
            cnx.close()
            response = ["succcess"]
        return JsonResponse(json.dumps(response), safe=False)


class displayActiveWork(APIView):
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
            value = 'true'
            query = ("SELECT * FROM workon_copy WHERE active = %s")
            cursor.execute(query, value)
            response = []
            results = cursor.fetchall()
            for row in results:
                jobID = row[0]
                jobNum = row[1]
                active = row[2]
                customer_ID = row[3]
                department_ID = row[4]
                partID = row[5]
                batchNumber = row[6]
                qtyOrdered = row[7]
                machineID= row[8]
                qty_finished = row[9]
                qty_scrap = row[10]
                response.append({'jobID': jobID, 'jobNum': jobNum, 'active': active, 'customer_ID': customer_ID,
                                 'department_ID': department_ID, 'partID': partID, 'machineID': machineID, 'qty_finished': qty_finished, 'qty_scrap': qty_scrap, 'qtyOrdered': qtyOrdered})
        finally:
            cursor.close()
            cnx.close()
        return JsonResponse(json.dumps(response), safe=False)


def vote(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("in here")
        hello = request.body
        print(hello)
        body_unicode = request.body.decode('utf-8')
        body_data = body_unicode
        print(body_data)
        print(request.POST.get('your_name'))
        print(request.POST.get('due_date'))
    return HttpResponse('Make sure all fields are entered and valid.')


def ReadBlob(request):
    print("in here getiing those blobs")
    conn = pymysql.connect(host="35.184.175.243",  # your host, usually localhost
                           user="root",  # your username
                           passwd="test12",  # your password
                           db="engineering")  # name of the data base
    try:
        cursor = conn.cursor()
        query = ("SELECT document_blob FROM technical_drawing WHERE drawingID = 129")
        cursor.execute(query)
        ablob = cursor.fetchone()[0]
        print(ablob)
        filename = "/home/dawdiken/test.PNG"
        # filename = "test.PNG"
        with open(filename, 'wb') as output_file:
            output_file.write(ablob)
        # return filename
    finally:
        cursor.close()
        conn.close()
        return HttpResponse(filename)


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
        return HttpResponse('Make sure all fields are entered and valid.')
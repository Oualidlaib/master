from django.db import connection
from django.http import HttpResponse
import re


def see_tables(request):
    query = "SELECT username, password last_name FROM auth_user"
    cursor = connection.cursor()
    cursor.execute(query)

    # Fetch the results and return them
    results = cursor.fetchall()
    return HttpResponse(results)


def vulnerable_view(request):
    if 'username' in request.GET and 'password' in request.GET:
        username = request.GET['username']
        password = request.GET['password']

        # This is where the SQL injection vulnerability lies
        query = "SELECT email FROM auth_user WHERE username = '%s' AND password = '%s' " % (
            username, password)
        cursor = connection.cursor()
        cursor.execute(query)

        # Fetch the results
        results = cursor.fetchall()

        # Close the cursor
        cursor.close()

        return HttpResponse(results)
    else:
        return HttpResponse(results)


def home(request):
    return HttpResponse("<h1>Hello, this is test web site</h1>")

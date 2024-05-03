from django.db import connection
from django.http import HttpResponse
import re


def see_tables(request):
    query = "SELECT username, email, first_name, last_name FROM auth_user"
    cursor = connection.cursor()
    cursor.execute(query)

    # Fetch the results and return them
    results = cursor.fetchall()
    return HttpResponse(results)


def vulnerable_view(request):
    if 'search' in request.GET:
        search_query = request.GET['search']

        # This is where the SQL injection vulnerability lies
        query = "SELECT * FROM  WHERE column_name = '%s'" % search_query
        cursor = connection.cursor()
        cursor.execute(query)

        # Fetch the results and return them
        results = cursor.fetchall()

        # Just for demonstration, printing the results
        for result in results:
            print(result)

        # Close the cursor
        cursor.close()

        return HttpResponse("Query executed successfully")
    else:
        return HttpResponse("No search query provided")

from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# views functions / paths:
# 1. index - (/..)
# 2. get_date - (/date)

def index(request):
    # create simple html page as a string
    template = "<html>" \
                "This is your first view" \
                "</html>"

    return HttpResponse(content=template)

def get_date(request):
    today = date.today()
    template = "<html>" \
                f"Today's date is {today}" \
                "</html>"

    return HttpResponse(content=template)




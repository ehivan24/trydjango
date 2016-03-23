from django.http import HttpResponse
from django.template.loader import get_template
import datetime
from django.template import Template, Context
from django.shortcuts import render_to_response
from django.http import Http404

def hello(request):

    link = """<html><body><a href='http://127.0.0.1:8000/current_datetime/'> current_date time </a>
    <div><a href='http://127.0.0.1:8000/my_page/'> My_page </a></div>
    <p><a href='http://127.0.0.1:8000/time/plus/13'> hours_ahead </a></p>
    <p> <a href='http://127.0.0.1:8000/current_datetime1/'> current_datetime1 </a></p>
    <p> <a href='http://127.0.0.1:8000/current_datetime2/'> current_datetime2 </a></p>
    <p> <a href='http://127.0.0.1:8000/current_datetime3/'> current_datetime3 </a></p>
    <p> <a href='http://127.0.0.1:8000/current_datetime4/'> current_datetime4 </a></p>
    </body></html>"""
    
    return HttpResponse(link)

def my_page(request):

    page = """
            <html>
            <body>
                <head> </head>
                <title> Welcome to Jamrock </title>
                <div><h1> Here we are testing Django </h1><p> Yes we are </p>


                <p>New P </p>

                <code> python manage.py runserver </code>
                <a href='http://127.0.0.1:8000/hello/'> link </a>
                
                </body>
            </html>
            """

    return HttpResponse(page)


def current_datetime(request):
    now = datetime.datetime.now()
    
    html1 = "<html><body>It is now %s.</body></html>" % now
            
    return HttpResponse(html1)


def hours_ahead(request, offset):

    # run http://127.0.0.1:8000/time/plus/1/
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hours, it will be %s <div>   </div></body></html>" % (offset, dt)

    return HttpResponse(html)


def current_datetime1(request):
    now = datetime.datetime.now()
    t = Template("<html><body>it is now {{ current_time }}</body></html>")
    html = t.render(Context({'current_time': now}))
    return HttpResponse(html)

    
def current_datetime2(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    name = 'Maria'
    html = t.render(Context({'current_date': now, 'username': name }))
    return HttpResponse(html)

def current_datetime3(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})
        

def current_datetime4(request):
    current_date = datetime.datetime.now()
    username = "Maria2"
    password = "thisPass"
    title = "learning Django"
    return render_to_response('current_datetime1.html', locals())


def View404(request, param):
    if not param:
        raise Http404
    return render_to_response('404.html')

    

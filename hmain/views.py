# To change this template, choose Tools | Templates
# and open the template in the editor.
# -*- coding: utf-8 -*-
from hmain.models import Event as Ev
#from multiprocessing import Event
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, delete_object, \
    update_object
from google.appengine.ext import db
from mimetypes import guess_type
from ragendja.dbutils import get_object_or_404
from ragendja.template import render_to_response
from hmain.models import Blog
from google.appengine.api import images

__author__="John"
__date__ ="$16.Kas.2010 14:47:06$"


def index(request):
    e = Ev.gql("order by event_date desc limit 4 ").fetch(4)
    b = Blog.gql("ORDER BY date DESC limit 10").fetch(10)
    return render_to_response(request, 'index.html',{'events':e,"blog":b})

def events_image(request,id):
    e = Ev.get(id.split("/")[0])

    return HttpResponse(images.resize(e.event_picture,320))

def events_imagethm(request,id):
    e = Ev.get(id.split("/")[0])
    return HttpResponse(images.resize(e.event_picture,120))

def blog(request):
    b = Blog.gql("ORDER BY date DESC limit 10").fetch(10)
    return render_to_response(request, 'blog.html',{"blog":b})

def blog_view(request,elm):
    #return HttpResponse(elm)
    b = Blog.gql("where rewrite ='"+elm+"' ORDER BY date DESC limit 10").fetch(1)
    return render_to_response(request, 'blog_view.html',{"blog":b})

def create_admin_user(request):
    user = User.get_by_key_name('admin')
    if not user or user.username != 'admin' or not (user.is_active and
            user.is_staff and user.is_superuser and
            user.check_password('admin')):
        user = User(key_name='admin', username='admin',
            email='admin@localhost', first_name='Boss', last_name='Admin',
            is_active=True, is_staff=True, is_superuser=True)
        user.set_password('admin')
        user.put()
    return HttpResponse("tamam")

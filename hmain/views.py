# To change this template, choose Tools | Templates
# and open the template in the editor.
# -*- coding: utf-8 -*-


from hmain.models import Event as Ev
#from multiprocessing import Event
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404 , HttpResponseRedirect

from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, delete_object, \
    update_object
from google.appengine.ext import db
from mimetypes import guess_type
from ragendja.dbutils import get_object_or_404
from ragendja.template import render_to_response 
from hmain.models import Blog ,Menus , MenuMain , Languages , Pages , guestbook as gg
from google.appengine.api import images
from plugins.fb import *
__author__="John"
__date__ ="$16.Kas.2010 14:47:06$"



def rendermain(request,tmp,params):
    langx = "English";
    if "lang" in request.session:
        langx = request.session['lang']


    parent = MenuMain.gql("where menuName = 'Main Page'").get()
    langs = Languages.gql("where lang_name = '"+langx+"'").get()
    menu = Menus.gql("where lang = :lang and menuParent = :parentm",lang=langs.key(),parentm=parent).fetch(100)

    langlist = Languages.all()

    #menu.filter("lang=", langs.key())
    #menu.filter("menuParent=",parent.key())
    #menu.filter("lang=",langs)
    #menu.filter("menuParent=",parent)
    params['menus'] = menu
    params['langlist'] = langlist
    return render_to_response(request, tmp,params)


from django import forms



def index(request):
    import datetime
    e = Ev.gql("where event_date > :dd order by event_date desc limit 4 ",dd=datetime.datetime.now()).fetch(4)
    b = Blog.gql("ORDER BY date DESC limit 3").fetch(3)
    return rendermain(request, 'index.html',{'events':e,"blog":b})

def eventlist(request):
    import datetime
    #d = datetime.datetime()
    e = Ev.gql("where event_date > :dd order by event_date desc limit 10 ",dd=datetime.datetime.now()).fetch(4)
    #e = str(datetime.datetime.now())
    return rendermain(request, 'events.html',{'events':e})



def booknow(request):
   
    #e = str(datetime.datetime.now())
    return rendermain(request, 'booknow.html',{})

def setlang(request,lang):

    request.session['lang'] =lang
    return HttpResponseRedirect("/")

def pages(request,page):

    p = Pages.gql("where rewrite = '"+page+"'").get()

    return rendermain(request, 'page_view.html',{"page":p,"rewrite":page})

def events_image(request,id):
    e = Ev.get(id.split("/")[0])

    return HttpResponse(images.resize(e.event_picture,320))

def events_imagethm(request,id):
    e = Ev.get(id.split("/")[0])
    return HttpResponse(images.resize(e.event_picture,120))

def writeguest(request):

    if "mail" in request.POST and "name" in request.POST and "review" in request.POST:
        a = gg()
        a.text = request.POST['review']
        a.froms = request.POST['name']
        a.from_mail = request.POST['mail']
        a.accesstoken = request.POST['access_token']
        a.save()
        if request.POST['access_token'] != "":
            f = facebookapp()
            r = request.POST['review']
            f.sendMessage("Write a review on guestbook", "http://hostel-dev.appspot.com/media/1/global/images/logo.png", r[:100] , "http://chillouthc.com/guestbook",request.POST['access_token'])
        return HttpResponseRedirect("/guestbook")

    return rendermain(request, 'guestbookw.html',{})

def guestbook(request):
    b = gg.gql("ORDER BY date DESC").fetch(10000)
    return rendermain(request, 'guestbook.html',{"guest":b})

def blog(request):
    b = Blog.gql("ORDER BY date DESC limit 10").fetch(10)
    return rendermain(request, 'blog.html',{"blog":b})

def blog_view(request,elm):
    #return HttpResponse(elm)
    b = Blog.gql("where rewrite ='"+elm+"' ORDER BY date DESC limit 10").fetch(1)
    return rendermain(request, 'blog_view.html',{"blog":b})

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

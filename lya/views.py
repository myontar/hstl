# To change this template, choose Tools | Templates
# and open the template in the editor.
# -*- coding: utf-8 -*-


from django.http import HttpResponse

from ragendja.template import render_to_response
from google.appengine.api import images
from google.appengine.api import memcache
from google.appengine.api import urlfetch
import json

__author__="John"
__date__ ="$16.Kas.2010 14:47:06$"


def getmenu(lang,parent):

    data = memcache.get("menu_%s_%s" % (lang,parent))

    if data == None:
        url = "http://localhost:8000/remote_db?mode=menu&parent="+parent+"&lang="+lang
        result = urlfetch.fetch(url)
        j = json.loads(result)
        data = j
        memcache.add(key="menu_%s_%s" % (lang,parent), value=j, time=86400)
    return data

def getpage(page,lang):
    data = memcache.get("page_%s_%s" % (lang,page))

    if data == None:
        url = "http://localhost:8000/remote_db?mode=page&page="+page+"&lang="+lang
        result = urlfetch.fetch(url)
        j = json.loads(result)
        data = j
        memcache.add(key="page_%s_%s" % (lang,page), value=j, time=86400)
    return data

def rendermain(request,tmp,params):
    langx = "English";
    if "lang" in request.session:
        langx = request.session['lang']
    menu = getmenu(langx,"Main Menu")

    #menu.filter("lang=", langs.key())
    #menu.filter("menuParent=",parent.key())
    #menu.filter("lang=",langs)
    #menu.filter("menuParent=",parent)
    params['menus'] = menu
    
    return render_to_response(request, tmp,params)


def remotecall(request):

    data = request.GET['data']
    lang = request.GET['lang']
    if request.GET['mode'] == "page":
    

    return rendermain(request,"index2.html",{})

def lang(request):
    request.session['lang'] = request.GET['lang']
    return render_to_response(request,"redirect.html",{"url":'/'})

def index(request):

    page = getpage("index_lya",request.session['lang'])
    return rendermain(request,"index2.html",{"page":page})
# -*- coding: utf-8 -*-
from django.db.models import permalink, signals
from google.appengine.ext import db
from ragendja.dbutils import cleanup_relations
from plugins.general import slug
from google.appengine.api import memcache
from plugins.fb import *
__author__="John"
__date__ ="$16.Kas.2010 14:29:47$"




class Languages(db.Model):
    lang_name = db.StringProperty(required=True)
    def __unicode__(self):
        return self.lang_name
    
    
signals.pre_delete.connect(cleanup_relations, sender=Languages)

class LangTexts(db.Model):
    lang        = db.ReferenceProperty(Languages, required=True, collection_name='lang_set')
    base_text   = db.StringProperty(required=True)
    text        = db.StringProperty(required=True)
    def __unicode__(self):
        return "%s -> %s" %  (self.lang.lang_name,self.base_text)
    def save(self):
        memcache.delete("lang_%s" % self.lang.lang_name)
        super(LangTexts, self).save()

class Gallery(db.Model):
    name = db.StringProperty(required=True)
    def __unicode__(self):
        return self.name

class GalleryLang(db.Model):
    lang        = db.ReferenceProperty(Languages, required=True, collection_name='lang_gallery')
    name        = db.StringProperty(required=True)

class GalleryFile(db.Model):
    gallery = db.ReferenceProperty(Gallery, required=True, collection_name='gallery')
    file    = db.BlobProperty()
    desc    = db.ReferenceProperty(GalleryLang, required=False, collection_name='gallerylang')
    def __unicode__(self):
        return self.gallery.name

class MenuMain(db.Model):
    menuName    = db.StringProperty(required=True)
    def __unicode__(self):
        return "%s" %  self.menuName


class Pages(db.Model):
    lang        = db.ReferenceProperty(Languages, required=True, collection_name='lang_page')
    pagename    = db.StringProperty(required=True,default='blank')
    pagetext    = db.TextProperty(required=True)
    last_edit   = db.DateTimeProperty()
    rewrite     = db.StringProperty(required=False)
    pageMenu    = db.ReferenceProperty(MenuMain, required=False, collection_name='page_menu')
    gallery = db.ReferenceProperty(Gallery, required=False, collection_name='gallery2')
    def save(self):
        self.rewrite = slug(self.pagename)
        super(Pages, self).save()
    def __unicode__(self):
        return "%s -> %s" %  (self.lang.lang_name,self.pagename)

class Menus(db.Model):
    lang        = db.ReferenceProperty(Languages, required=True, collection_name='lang_menu')
    name        = db.StringProperty(required=True)
    menuParent  = db.ReferenceProperty(MenuMain, required=False, collection_name='parent_menu')
    menugopage  = db.IntegerProperty(default=1)
    menupage    = db.ReferenceProperty(Pages, required=False, collection_name='page_Set')
    menugourl   = db.StringProperty(required=False)
    def __unicode__(self):
        return "%s -> %s" %  (self.lang.lang_name,self.name)



class Event(db.Model):
    event_name      = db.StringProperty(required=True)
    event_picture   = db.BlobProperty(required=True)
    event_venue     = db.StringProperty(required=True)
    event_date      = db.DateTimeProperty(required=True)
    def __unicode__(self):
        return self.event_name
    
class EventDesc(db.Model):
    lang        = db.ReferenceProperty(Languages, required=True, collection_name='lang_evt')
    desc        = db.StringProperty()
    event       = db.ReferenceProperty(Event, required=True, collection_name='evt')



class Rooms(db.Model):
    room_name   = db.StringProperty()

class guestbook(db.Model):
    text        = db.TextProperty()
    date        = db.DateTimeProperty(auto_now_add = True,auto_now=True)
    froms       = db.StringProperty()
    from_mail   = db.StringProperty()
    accesstoken = db.StringProperty(required=False)
class Blog(db.Model):
    title       = db.StringProperty()
    tags        = db.StringProperty()
    text        = db.TextProperty()
    rewrite     = db.StringProperty(required=False)
    date        = db.DateTimeProperty(auto_now_add = True,auto_now=True)
    def save(self):

        import re
        r = re.sub(r'<[^>]*?>', '', self.text)
        self.rewrite = slug(self.title)
        a = facebookapp()
        a.sendMessage(self.title, "http://hostel-dev.appspot.com/media/1/global/images/logo.png", r[:100] , "http://chillouthc.com/blog/"+self.rewrite)
        
        super(Blog, self).save()
    def __unicode__(self):
        return "%s - %s " % (self.title , str(self.date))

class Books(db.Model):
    name            = db.StringProperty()
    surname         = db.StringProperty()
    telephone       = db.StringProperty()
    email           = db.EmailProperty()
    country         = db.StringProperty()
    room            = db.StringProperty()
    adult           = db.IntegerProperty()
    arrival_date    = db.DateTimeProperty()
    departure_date  = db.DateTimeProperty()
    arrival_time    = db.StringProperty()
    message         = db.StringProperty()
    
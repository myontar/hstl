# -*- coding: utf-8 -*-
from django.db.models import permalink, signals
from google.appengine.ext import db
from ragendja.dbutils import cleanup_relations
from plugins.general import slug
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
    
class Pages(db.Model):
    lang        = db.ReferenceProperty(Languages, required=True, collection_name='lang_page')
    pageName    = db.StringProperty(required=True)
    pageText    = db.TextProperty(required=True)
    last_edit   = db.DateTimeProperty()
    def __unicode__(self):
        return "%s -> %s" %  (self.lang.lang_name,self.pageName)

class Gallery(db.Model):
    name = db.StringProperty(required=True)
    def __unicode__(self):
        return self.name

class GalleryFile(db.Model):
    gallery = db.ReferenceProperty(Gallery, required=True, collection_name='gallery')
    file    = db.BlobProperty()
    def __unicode__(self):
        return self.gallery.name

class MenuMain(db.Model):
    lang        = db.ReferenceProperty(Languages, required=True, collection_name='lang_menuparnt')
    menuName    = db.StringProperty(required=True)
    def __unicode__(self):
        return "%s -> %s" %  (self.lang.lang_name,self.menuName)

class Menus(db.Model):
    lang        = db.ReferenceProperty(Languages, required=True, collection_name='lang_menu')
    menuName    = db.StringProperty(required=True)
    menuParent  = db.ReferenceProperty(MenuMain, required=False, collection_name='parent_menu')
    menuGoPage  = db.IntegerProperty(default=1)
    menuPage    = db.ReferenceProperty(Pages, required=False, collection_name='page_Set')
    menuGoUrl   = db.StringProperty(required=False)
    def __unicode__(self):
        return "%s -> %s" %  (self.lang.lang_name,self.menuName)



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

class Blog(db.Model):
    title       = db.StringProperty()
    tags        = db.StringProperty()
    text        = db.TextProperty()
    rewrite     = db.StringProperty(required=False)
    date        = db.DateTimeProperty(auto_now_add = True,auto_now=True)
    def save(self):
        self.rewrite = slug(self.title)
        super(Blog, self).save()
    def __unicode__(self):
        return "%s - %s " % (self.title , str(self.date))
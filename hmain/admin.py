# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="John"
__date__ ="$16.Kas.2010 14:43:01$"

from django.contrib import admin
from hmain.models import Languages,Pages,LangTexts,Menus,MenuMain,Event,EventDesc,Rooms,Blog,Gallery,GalleryFile



admin.site.register(Languages)
admin.site.register(Pages)
admin.site.register(LangTexts)
admin.site.register(Menus)
admin.site.register(MenuMain)
admin.site.register(Event)
admin.site.register(EventDesc)
admin.site.register(Rooms)
admin.site.register(Blog)
admin.site.register(Gallery)
admin.site.register(GalleryFile)
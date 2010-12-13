# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="John"
__date__ ="$16.Kas.2010 14:43:01$"

from django.contrib import admin
from hmain.models import Languages,Pages,LangTexts,Menus,MenuMain,Event,EventDesc,Rooms,Blog,Gallery,GalleryFile,guestbook


class langAdmin(admin.ModelAdmin):
    search_fields = ["base_text","lang"]
    list_filter   = ["base_text","lang"]
    list_display   = ('base_text', 'lang','text')

class menuAdmin(admin.ModelAdmin):
    list_display   = ('name' , 'menuParent', 'lang')
class guestbooka(admin.ModelAdmin):
    list_display   = ('froms' , 'text', 'date')

admin.site.register(Languages)
admin.site.register(guestbook,guestbooka)
admin.site.register(Pages)
admin.site.register(LangTexts,langAdmin)
admin.site.register(Menus,menuAdmin)
admin.site.register(MenuMain)
admin.site.register(Event)
admin.site.register(EventDesc)
admin.site.register(Rooms)
admin.site.register(Blog)
admin.site.register(Gallery)
admin.site.register(GalleryFile)
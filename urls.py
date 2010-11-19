# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from ragendja.urlsauto import urlpatterns
from ragendja.auth.urls import urlpatterns as auth_patterns
from django.contrib import admin

admin.autodiscover()

handler500 = 'ragendja.views.server_error'

urlpatterns = auth_patterns + patterns('',
    ('^admin/(.*)', admin.site.root),
    (r'^$', 'hmain.views.index'),
    (r'^blog$', 'hmain.views.blog'),
    (r'^blog/(.*)$', 'hmain.views.blog_view'),
    (r'^evtimage/(.*)/thm$', 'hmain.views.events_imagethm'),
    (r'^create_admin_user$', 'hmain.views.create_admin_user'),


    (r'^evtimage/(.*)$', 'hmain.views.events_image'),
    
    

    # Override the default registration form
   # url(r'^account/register/$', 'registration.views.register',
   #     kwargs={'form_class': UserRegistrationForm},
   #     name='registration_register'),
) + urlpatterns

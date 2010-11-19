# To change this template, choose Tools | Templates
# and open the template in the editor.
from django import template

register = template.Library()
__author__="John"
__date__ ="$18.Kas.2010 16:55:20$"


@register.filter
def limittext(text,url):
    if len(text) > 300:
        return text[:300]+"... <a href='blog/"+str(url)+"'>read more</a>"
    else:
        return text
register.filter('limittext', limittext)

@register.filter
def formatdate(d):
    return d.strftime("%b<br/><span>%d</span><br />%H:%M")

register.filter('formatdate', formatdate)

@register.filter
def gdate(d,format):
    return d.strftime(str(format))

register.filter('gdate', gdate)

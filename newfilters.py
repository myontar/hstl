# To change this template, choose Tools | Templates
# and open the template in the editor.
from django import template

register = template.Library()
__author__="John"
__date__ ="$18.Kas.2010 16:55:20$"


@register.filter
def limittext(value):
    return text[:200]+"..."
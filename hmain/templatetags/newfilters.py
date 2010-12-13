# To change this template, choose Tools | Templates
# and open the template in the editor.
from django import template
from google.appengine.api import memcache
from hmain.models import Languages , LangTexts , Menus 

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


class getLang(template.Node):
    def __init__(self, format_string):
        self.format_string = format_string
    def render(self, context):

        request = context['request']
        if "lang" in request.session:
            lang_s = request.session['lang']
        else:
            lang_s = "English"
        

        lang = memcache.get("lang_%s" % (lang_s))
        cache = 1
        if lang == None:
            cache = 0
            langs = Languages.gql("where lang_name = '"+lang_s+"'").get()
            langData = LangTexts.gql("where lang = :lang",lang=langs.key()).fetch(1000)
            lang = {}
            for i in langData:
                lang[i.base_text] = i.text
            memcache.add("lang_%s" % (lang_s), lang , 100000)

        if self.format_string in lang:

            return lang[self.format_string]
        else:
            if cache == 1:
                langs = Languages.gql("where lang_name = '"+lang_s+"'").get()
                langData = LangTexts.gql("where lang = :lang",lang=langs.key()).fetch(1000)
                lang = {}
                for i in langData:
                    lang[i.base_text] = i.text
                memcache.add("lang_%s" % (lang_s), lang , 100000)
                if self.format_string in lang:
                    return lang[self.format_string]
                else:
                    return "Please add baselang for %s to %s" % (lang_s,self.format_string)
            else:
                return "Please add baselang for %s to %s" % (lang_s,self.format_string)



class getMenu(template.Node):
    def __init__(self, format_string):
        self.format_string = template.Variable(format_string)
    def render(self, context):
        try:
            if self.format_string.resolve(context) != None:
                a = Menus.gql("where menuParent = :parent",parent=self.format_string.resolve(context)).fetch(100)
                text = ""
                for i in a:
                    if i.menugopage == 1:
                        text = text + """<a href="%s" id="page_%s" class="menu1">%s</a>  """ % (i.menupage.rewrite,i.menupage.rewrite,i.name)
                    else:
                        text = text + """<a href="%s" class="menu1" >%s</a>  """ % (i.menugourl,i.name)
                if text != "":
                    text = """  <div id="menu" style="float:right;margin:0;margin-right:10px;">  """+text+"</div>"

                return text
            else:
                return ""
        except:
            return ""
@register.tag
def do_menu(parser,token):
    try:
    # split_contents() knows not to split quoted strings.
        tag_name, format_string = token.split_contents()
    except:
        pass

    return getMenu(format_string)
register.tag('menu', do_menu)

@register.tag
def do_lang(parser, token):
    try:
    # split_contents() knows not to split quoted strings.
        tag_name, format_string = token.split_contents()
    except:
        pass
    return getLang(format_string[1:-1])

register.tag('lang', do_lang)
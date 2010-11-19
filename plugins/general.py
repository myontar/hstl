import re
def slug(text):
   
    re_strip = re.compile(r'[^\w\s-]')
    #text =  text.decode("utf-8")
    tmp = text.lower()
    #tmp = text.lower()
    re_dashify = re.compile(r'[-\s]+')
    cleanup= re_strip.sub('', tmp).strip().lower()
    return re_dashify.sub('-', cleanup)
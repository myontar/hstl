var LANGUAGE_CODE="de";var LANGUAGE_BIDI=false;var catalog=new Array();function pluralidx(a){return(a==1)?0:1}function gettext(a){var b=catalog[a];if(typeof(b)=="undefined"){return a}else{return(typeof(b)=="string")?b:b[0]}}function ngettext(b,a,c){value=catalog[b];if(typeof(value)=="undefined"){return(c==1)?b:a}else{return value[pluralidx(c)]}}function gettext_noop(a){return a}function interpolate(b,c,a){if(a){return b.replace(/%\(\w+\)s/g,function(d){return String(c[d.slice(2,-2)])})}else{return b.replace(/%s/g,function(d){return String(c.shift())})}}window.hgettext=function(a){return gettext(a)};window.hngettext=function(b,a,c){return ngettext(b,a,c)};jQuery(document).ready(function(){main.events();main.animate("#blt1",1);main.animate("#blt2",1.9);main.animate("#blt3",2)});var eventList=new Array();var eventL=new Array();var evt=0;var main={animate:function(c,a){var b=jQuery(c).css("left");jQuery(c).animate({left:-300},6000*a,"linear",function(){jQuery(c).css("left",jQuery("body").width()+300);jQuery(c).animate({left:b},20000*a,"linear",function(){main.animate(c,a)})})},events:function(){jQuery(".events").css("display","none");jQuery(".events").each(function(){eventList.push(jQuery(this))});jQuery(".ed > a").each(function(){eventL.push(jQuery(this))});main.eventsHold()},eventsHold:function(){if(evt==0){if(eventList[eventList.length-1].css("display")=="block"){eventList[eventList.length-1].fadeOut("slow",function(){eventList[eventList.length-1].hide();eventList[evt].fadeIn("slow");jQuery(".ed > a > img").attr("src",media+"images/point1.png");eventL[evt].find("img").attr("src",media+"images/point2.png");evt++;if(evt==eventList.length){evt=0}setTimeout("main.eventsHold();",10000)})}else{eventList[evt].fadeIn("slow");jQuery(".ed > a > img").attr("src",media+"images/point1.png");eventL[evt].find("img").attr("src",media+"images/point2.png");evt++;if(evt==eventList.length){evt=0}setTimeout("main.eventsHold();",10000)}}else{if(eventList[evt]){eventList[evt-1].fadeOut("slow",function(){eventList[evt-1].hide();eventList[evt].fadeIn("slow");jQuery(".ed > a > img").attr("src",media+"images/point1.png");eventL[evt].find("img").attr("src",media+"images/point2.png");evt++;if(evt==eventList.length){evt=0}setTimeout("main.eventsHold();",10000)})}else{if(eventList[evt-1]){evt++;if(evt==eventList.length){evt=0}setTimeout("main.eventsHold();",10000)}}}}};
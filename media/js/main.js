
jQuery(document).ready(function() {

main.events();
main.animate("#blt1",1);
main.animate("#blt2",1.9);
main.animate("#blt3",2);
});
var eventList = new Array();
var eventL    = new Array();
var evt       = 0;
var main      = {
    animate:function(elm,re) {
        
        var nowLeft = jQuery(elm).css("left");
        jQuery(elm).animate(
            {left:-300},6000 * re,"linear",function() {
                
                jQuery(elm).css("left",jQuery("body").width()+300);
                 jQuery(elm).animate(
                    {left:nowLeft},20000 * re,"linear",function() {
                        main.animate(elm,re);
                    });
            }
        );
    },
    events:function() {
        jQuery(".events").css("display","none");
        
        jQuery(".events").each(function() {
            eventList.push(jQuery(this));
        });
        jQuery(".ed > a").each(function() {
            eventL.push(jQuery(this));
        });
        main.eventsHold();
    },
    eventsHold:function() {
      if(evt == 0) {
          
          if(eventList[eventList.length-1].css("display") == "block") {
              eventList[eventList.length-1].fadeOut("slow",function() {
                  eventList[eventList.length-1].hide();
                  eventList[evt].fadeIn("slow");
                  jQuery(".ed > a > img").attr("src",media+"images/ico.png");
                  eventL[evt].find("img").attr("src",media+"images/ico2.png");
                  evt++;
                  if(evt == eventList.length) evt = 0;
                  setTimeout("main.eventsHold();",10000);

          });
          } else {
              eventList[evt].fadeIn("slow");
              jQuery(".ed > a > img").attr("src",media+"images/ico.png");
              eventL[evt].find("img").attr("src",media+"images/ico2.png");
              evt++;
              if(evt == eventList.length) evt = 0;
              setTimeout("main.eventsHold();",10000);
          }
      } else {
          if(eventList[evt]) {
              eventList[evt-1].fadeOut("slow",function() {
                  eventList[evt-1].hide();
                  eventList[evt].fadeIn("slow");
                  jQuery(".ed > a > img").attr("src",media+"images/ico.png");
                  eventL[evt].find("img").attr("src",media+"images/ico2.png");
                  evt++;
                  if(evt == eventList.length) evt = 0;
                  setTimeout("main.eventsHold();",10000);
                });
          } else {
               if(eventList[evt-1]) {
                   evt++;
                   if(evt == eventList.length) evt = 0;
                   setTimeout("main.eventsHold();",10000);
               }
          }
      }
      
      
    }
}

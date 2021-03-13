pip install psutil
pip install plyer
from plyer import notification

import psutil
battery = psutil.sensors_battery()

plugged = battery.power_plugged

if __name__=="__main__": 
    if plugged:
        percent = battery.percent
        if percent <= 80:
            notification.notify( 
            #title of notification
            title = "Plugged In", 

            #message of notification
            message=" बेहतर बैटरी जीवन के लिए, 80% तक चार्ज करें" , 
            
            # displaying time 
            timeout=2 
            )
           
        elif percent == 100: 
            notification.notify( 
            title = "Plugged In", 
            message="कृपया चार्जर प्लग आउट करें। बैटरी चार्ज है" , 
            timeout=2 
            )
           
        else :
            notification.notify( 
            title = "Plugged In", 
            message="कृपया चार्जर निकालें। 80% तक बेहतर बैटरी जीवन शुल्क" , 
            timeout=2 
            )

    else:
        percent = battery.percent
        if percent <=20:
            notification.notify( 
            title = "Battery Reminder", 
            message="आपकी बैटरी कम चल रही है। आप अपने पीसी में प्लग इन करना चाह सकते हैं" , 
            timeout=2 
            )
       
        elif percent <=50:
            notification.notify( 
            title = "Battery Reminder", 
            message=f" Battery is {percent}." ,
            timeout=2 
            )
        
        elif percent == 100:
            notification.notify( 
            title = "Battery Reminder", 
            message="पूर्णतःउर्जित" , 
            timeout=2 
            )

        else:
            notification.notify( 
            title = "Battery Reminder", 
            message=f"Battery is {percent}" , 
            timeout=2 
            )

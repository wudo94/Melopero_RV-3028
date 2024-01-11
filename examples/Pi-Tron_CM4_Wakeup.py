import melopero_RV_3028 as mp
import time
from datetime import datetime
 
rtc = mp.RV_3028()
rtc.set_12h_format(False)
 
time = rtc.get_time()
# returns a dictionary containg information about the time
print(time)
 
date = rtc.get_date()
# returns a dictionary containg information about the date
print(date)
 
datetimertc = rtc.get_datetime()
# returns a dictionary containg information about the date and time
print(datetimertc)
 
# First disable other sources of interrupts
rtc.enable_timer(enable=False, repeat=False, generate_interrupt=False)
rtc.enable_periodic_time_update_interrupt(generate_interrupt=False)
rtc.clear_interrupt_flags()
current_datetime = datetime.now()
print(current_datetime)
 
#time.sleep(1)
print("Enable Alarm!")
 
# set the alarm to trigger 10 minutes from now
minute_alarm = current_datetime.minute + 10 % 60
rtc.set_minute_alarm(minute_alarm)
rtc.enable_alarm(enable=True, generate_interrupt=True)
print("Alarm set to trigger ten minutes from now...")
#print("The alarm will trigger every hour at minute {}".format(minute_alarm)

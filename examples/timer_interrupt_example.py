#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Leonardo La Rocca
"""

import melopero_RV_3028 as mp
import datetime
import gpiozero as gpio
from signal import pause

def main():
    # First initialize and create the rtc device
    rtc = mp.RV_3028()
    # Set the device to use the 24hour format (default) instead of the 12 hour format
    rtc.set_12h_format(False)

    # Then set the date and time.
    # retrieve the datetime from the library datetime
    current_datetime = datetime.datetime.now()

    # set the date and time for the device
    rtc.set_time(current_datetime.hour, current_datetime.minute, current_datetime.second)
    rtc.set_date(current_datetime.weekday(), current_datetime.day, current_datetime.month, current_datetime.year % 2000)

    # set the timer to repeatedly fire after 10 seconds
    rtc.set_timer(10, mp.RV_3028.TIMER_FREQ_1Hz)
    rtc.enable_timer(enable=True, repeat=True, generate_interrupt=True)

    # set the pin to listen to interrupts
    int_listener_pin = 7  # gpio4
    interrupt = gpio.Button(int_listener_pin)
    interrupt.when_pressed = on_interrupt

    pause()


def on_interrupt():
    print("Timer: beep beep")


if __name__ == "__main__":
    main()
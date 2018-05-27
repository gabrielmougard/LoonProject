import time
from threading import Thread
import os
import RPi.GPIO as GPIO


#helper functions#########

def send_data(data):
    output = open('data.dat','a')
    output.write("\n{}".format(data[0],data[1]))
    output.close()

def send_data_POST_OP(data):
    output = open('POST.dat','a')
    output.write("\n{}\t{}".format(data[0],data[1]))
    output.close()

def get_data():

    try:
        dat_file = open('data.dat', 'r')
        old = ""
        for line in dat_file:
            if old:
                pass
            old = line

        if old:
            line = old

        dat_file.close()
        os.system('sudo rm /home/pi/Desktop/TIPE/data.dat')
        return line

    except FileNotFoundError:
        pass
####################


class AsyncBlinking(Thread):

    def __init__(self,pin,func):
        Thread.__init__(self)
        self.blink_time = 0.05
        self.func = func
        self.pin = pin


    def run(self):
        """code du thread de clignotement"""

        GPIO.output(self.pin,True)
        exec(self.func)
        time.sleep(self.blink_time)
        GPIO.output(self.pin,False)


class AsyncMesure(Thread):


    def __init__(self,sensor):
        Thread.__init__(self)
        self.sensor = sensor
        self.FREQUENCY_SECONDS = 0.1



    def run(self):
        """code du thread de mesure"""
        R_ALT = AsyncBlinking(21, "AsyncMesure.sensor.read_altitude()")
        S_DAT = AsyncBlinking(26,"send_data(AsyncMesure.sensor.read_altitude())")
        S_DAT_POST = AsyncBlinking(16,"send_data_POST_OP([AsyncMesure.sensor.read_altitude(), time.clock()])")

        time.clock()

        while True:
            R_ALT.start()
            S_DAT.start()
            S_DAT_POST.start()

            R_ALT.join()
            S_DAT.join()
            S_DAT_POST.join()
            time.sleep(self.FREQUENCY_SECONDS)






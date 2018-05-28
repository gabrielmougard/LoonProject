import time
from threading import Thread
import os
import RPi.GPIO as GPIO
import BMP085
import I2C
import smbus

t0 = time.time()

#helper functions#########

def send_data(data):
    output = open('/home/pi/Desktop/TIPE/data.dat','a')
    output.write("\n{}\t{}".format(data[0],data[1]))
    output.close()

def send_data_POST_OP(data):
    output = open('/home/pi/Desktop/TIPE/POST.dat','a')
    output.write("\n{}\t{}".format(data[0],data[1]))
    output.close()

def get_data():

    try:
        dat_file = open('/home/pi/Desktop/TIPE/data.dat', 'r')
        line = dat_file.readlines()[-1]
        dat_file.close()
        
        #line hold a variable with the shape 'XXX\tXXX\n'
        # we just want the first characters before \t
        
        res = []
        for elt in line:
            if elt == '\t':
                return float(''.join(res))
            res.append('{}'.format(elt))
    except "FileNotFoundError":
        return 0
    
####################


class AsyncBlinking(Thread):

    def __init__(self,pin,func):
        Thread.__init__(self)
        self.blink_time = 0.05
        self.func = func ##string
        self.pin = pin
        self.FREQUENCY_SECONDS = 0.1


    def run(self):
        """code du thread de clignotement"""
        while True:
            
            GPIO.output(self.pin,True)
            exec(self.func)
            time.sleep(self.blink_time)
            GPIO.output(self.pin,False)
            time.sleep(self.FREQUENCY_SECONDS)


class AsyncMesure(Thread,BMP085.BMP085):


    def __init__(self,sensor):
        Thread.__init__(self)
        self.sensor = sensor
       

    def run(self):
        """code du thread de mesure"""
        R_ALT = AsyncBlinking(21, "BMP085.BMP085().read_altitude()")
        S_DAT = AsyncBlinking(26,"send_data([BMP085.BMP085().read_altitude(),time.time()-t0])")
        S_DAT_POST = AsyncBlinking(16,"send_data_POST_OP([BMP085.BMP085().read_altitude(), time.time()-t0])")

        R_ALT.start()
        S_DAT.start()
        S_DAT_POST.start()

        R_ALT.join()
        S_DAT.join()
        S_DAT_POST.join()
        






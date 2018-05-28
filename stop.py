import RPi.GPIO as GPIO

GPIO.output(16,False) #S_DAT_POST()
GPIO.output(18,False) #servo
GPIO.output(20,False) #G_DAT()
GPIO.output(21,False) #R_ALT()
GPIO.output(26,False) #S_DAT()

GPIO.cleanup()

import RPi.GPIO as GPIO
import BMP085
import AsyncAsserv


####CONSTANTES#######
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT) #S_DAT_POST()
GPIO.setup(18,GPIO.OUT) #servo
GPIO.setup(20,GPIO.OUT) #G_DAT()
GPIO.setup(21,GPIO.OUT) #R_ALT()
GPIO.setup(26,GPIO.OUT) #S_DAT()

ajoutAngle = 5

ANGLE_FERMETURE = 0
duty1 = float(ANGLE_FERMETURE)/10 + ajoutAngle

ANGLE_OUVERTURE = 45
duty2 = float(ANGLE_OUVERTURE)/10 + ajoutAngle

pwm = GPIO.PWM(18,100) # pwm à 100Hz
pwm.start(5) #on commence à 5% du dutycycle (-90°)

sensor = BMP085.BMP085() #initialisation de l'altimètre
ALT_MAX  = sensor.read_altitude() + 2 #la consigne est à 2m au-dessus de la base de lancement


####################


#Creation du thread
asservissement = AsyncAsserv(duty1,duty2,pwm,sensor,ALT_MAX) #thread1



#Lancement du thread
asservissement.start()


#Attend que le thread se termine (sauf que celui-ci ne se termine pas
#donc c'est une boucle infinie...)

asservissement.join()


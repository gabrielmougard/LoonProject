from threading import Thread
import AsyncMesure
import time

class AsyncAsserv(Thread):
    """Thread chargé d'effectuer l'asservissement en parallèle des mesures"""

    def __init__(self,duty1,duty2,pwm,sensor,ALT_MAX):
        Thread.__init__(self)
        self.mesure = AsyncMesure(sensor)
        self.duty1 = duty1
        self.duty2 = duty2
        self.pwm = pwm
        self.ALT_MAX = ALT_MAX

    def run(self):
        """Code à executer pendant l'execution du Thread"""

        self.mesure.start() #demarrage du thread de mesure

        while True:

            altitude = AsyncMesure.get_data()
            altitude = float(altitude)

            if altitude > self.ALT_MAX: #fermeture
                self.pwm.ChangeDutyCycle(self.duty1)
            else: #ouverture
                self.pwm.ChangeDutyCycle(self.duty2)



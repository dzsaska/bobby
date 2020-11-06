#!/usr/bin/python3

import RPi.GPIO as GPIO

class Fan:
    def __init__( self, pin, f_pwm ):
        self._pin = pin
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup( self.pin, GPIO.OUT)

        self._pwm_out = GPIO.PWM( self.pin, f_pwm )
        self._pwm_out.start(0)

        self.speed = 50

    @property
    def pin(self):
        return self._pin

    @property
    def speed(self):
        return 100 - self._duty_cycle
    
    @speed.setter
    def speed(self, value):
        if value > 100:
            value = 100
        elif value < 0:
            value = 0

        self._duty_cycle = 100 - value
        self._pwm_out.ChangeDutyCycle( self._duty_cycle )        
    
    def kill(self):
        print("\"Oof\" - fan")
        self._pwm_out.stop()


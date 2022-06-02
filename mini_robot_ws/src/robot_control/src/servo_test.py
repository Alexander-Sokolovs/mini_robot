from gpiozero import Servo
import time
import pigpio

servo = 4
servo2 = 17
  
pwm = pigpio.pi() 
pwm.set_mode(servo, pigpio.OUTPUT)
pwm.set_mode(servo2, pigpio.OUTPUT)
 
pwm.set_PWM_frequency( servo, 50 )
pwm.set_PWM_frequency( servo2, 50 )


continuous = True


if continuous == True:
    min = 1370
    max = 1600
else:
    min = 700
    max = 2400

diff = max-min


# pwm.set_servo_pulsewidth( servo, 1490 )

 
while True:
    for i in range(min, max):
        pwm.set_servo_pulsewidth( servo, i )
        pwm.set_servo_pulsewidth( servo2, i )
        print(i)
        time.sleep( 0.1 )
    for i in range(diff):
        pwm.set_servo_pulsewidth( servo, max-i )
        pwm.set_servo_pulsewidth( servo2, max-i )
        print(max-i)
        time.sleep( 0.1 )
 
# turning off servo
pwm.set_PWM_dutycycle(servo, 0)
pwm.set_PWM_frequency( servo, 0 )
pwm.set_PWM_dutycycle(servo2, 0)
pwm.set_PWM_frequency( servo2, 0 )
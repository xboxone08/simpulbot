from gpiozero import LED, LightSensor, Robot, Button
from bluedot import BlueDot
from signal import pause
from time import sleep
from os import system

health = 25

dot = BlueDot(power_up_device=True)
dot.color = "#00CC66"
## dot.allow_pairing(None)
dot.wait_for_connection()

bot = Robot(left=(4, 14), right=(22, 23))
l_laser = LED(17)
r_laser = LED(5)
l_receptor = LightSensor(6)
r_receptor = LightSensor(27)


def move(pos) -> None:
    if pos.top:
        bot.forward(pos.distance)
        print(f"fwd {int(round(pos.distance * 100, 0))}%")
    elif pos.bottom:
        print(f"bckwd {int(round(pos.distance * 100, 0))}%")
        bot.backward(pos.distance / 2)
    elif pos.left:
        print(f"lft {int(round(pos.distance * 100, 0))}%")
        bot.left(pos.distance)
    elif pos.right:
        print(f"rght {int(round(pos.distance * 100, 0))}%")
        bot.right(pos.distance)


def shoot(pos) -> None:
    if pos.left:
        print("pew")
        l_laser.on()
        sleep(0.2)
        l_laser.off()
    elif pos.right:
        print("pew")
        r_laser.on()
        sleep(0.2)
        r_laser.off()
    elif pos.middle:
        print("PEW")
        l_laser.on()
        r_laser.on()
        sleep(0.2)
        l_laser.off()
        r_laser.off()


def stop() -> None:
    print("SCREECH")
    bot.stop()


def clean_up() -> None:
    dot.stop()
    raise SystemExit


def hurt() -> None:
    print("OW!")
    health -= 1

def shutdown() -> None:
    system("shutdown -h now")


dot.when_pressed = move
dot.when_moved = move
dot.when_double_pressed = shoot
dot.when_client_disconnects = clean_up
dot.when_released = stop

pause()

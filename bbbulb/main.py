from gpiozero import TimeOfDay, LED, MotionSensor
from datetime import time
from bluedot import BlueDot
from signal import pause
from time import sleep

dot = BlueDot(power_up_device=True)
dot.color = "#FFFFFF"
## dot.allow_pairing(None)
mot_det = MotionSensor(10)
hourglass = TimeOfDay(time(19, 30), time(6))
bulb = LED(14)
mode = "auto"


def on():
    global mode
    if (mode == "auto" and mot_det.motion_detected) or mode == "on":
        bulb.on()
        dot.color = "#FFFFFF"
    print("on")


def set_mode(val: str):
    global mode
    assert val == "auto" or val == "on"
    mode = val
    if val == "on":
        on()
    print(F"set mode to {mode}")


def toggle_mode():
    global mode
    if mode == "auto":
        dot.square = True
        set_mode("on")
        on()
    elif mode == "on":
        dot.square = False
        set_mode("auto")
    print("toggled mode")


def off(dev):
    global mode
    if mode == "on":
        return None
    bulb.off()
    dot.color = "#000000"
    print("off")


hourglass.when_activated = on
hourglass.when_deactivated = off
mot_det.when_no_motion = off
dot.when_pressed = lambda: toggle_mode()

pause()

import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
import board
import digitalio

led_onboard = digitalio.DigitalInOut(board.LED)
led_onboard.direction = digitalio.Direction.OUTPUT

btn1_pin = board.GP0
btn2_pin = board.GP2
btn3_pin = board.GP5
btn4_pin = board.GP7
btn5_pin = board.GP10
btn6_pin = board.GP14

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN

btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN

keyboard = Keyboard(usb_hid.devices)

buttons = {
    btn1: (Keycode.ALT, Keycode.F4),
    btn2: (Keycode.CONTROL, Keycode.F8),
    btn3: (Keycode.CONTROL, Keycode.F9),
    btn4: (Keycode.CONTROL, Keycode.ALT, Keycode.O),
    btn5: (Keycode.SHIFT, Keycode.ALT, Keycode.F),
    btn6: (Keycode.ALT, Keycode.FORWARD_SLASH),
}

pressed = {button: False for button in buttons}

while True:
    for button, keycode in buttons.items():
        if button.value and not pressed[button]:
            keyboard.send(*keycode)
            pressed[button] = True
        elif not button.value:
            pressed[button] = False
    time.sleep(0.1)

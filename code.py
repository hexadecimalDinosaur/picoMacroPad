import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

keybinds = (
        (Keycode.F13,),
        (Keycode.F14,),
        (Keycode.F15,),
        (Keycode.F16,),
        (Keycode.GUI, Keycode.UP_ARROW,),
        (Keycode.ALT, Keycode.TAB,),
        (Keycode.GUI, Keycode.LEFT_ARROW,),
        (Keycode.GUI, Keycode.DOWN_ARROW,),
        (Keycode.GUI, Keycode.RIGHT_ARROW,),
)

pins = (
    board.GP28,
    board.GP2,
    board.GP5,
    board.GP27,
    board.GP11,
    board.GP7,
    board.GP19,
    board.GP17,
    board.GP14,
)

buttons = []
for pin in pins:
    buttons.append(digitalio.DigitalInOut(pin))
    buttons[-1].direction = digitalio.Direction.INPUT
    buttons[-1].pull = digitalio.Pull.DOWN
buttons = tuple(buttons)

button_states = [False]*len(buttons)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

keyboard = Keyboard(usb_hid.devices)

size = len(buttons)

while True:
    led.value = True
    for i in range(size):
        if buttons[i].value and not button_states[i]:
            print(i, "pressed")
            button_states[i] = True
            for key in keybinds[i]:
                keyboard.press(key)
        elif not buttons[i].value and button_states[i]:
            print(i, "released")
            button_states[i] = False
            # for key in keybinds[i][::-1]:  # stepping not implemented in circuitpython yet
            for j in range(len(keybinds[i])-1,-1,-1):
                key = keybinds[i][j]
                keyboard.release(key)

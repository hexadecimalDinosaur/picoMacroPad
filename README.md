# Raspberry Pi Pico Macropad Firmware

Firmware for using a Raspberry Pi Pico as a macropad. I use the 9 key design by [hyperglu](https://cults3d.com/en/3d-model/gadget/bloko-9-pico) on cults3d.

## Installation

1. Wire up your Raspberry Pi Pico and keys

2. Install the latest version of [CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/) to your Raspberry Pi Pico

3. Install `adafruit_hid` library from the [CircuitPython Library Bundle](https://circuitpython.org/libraries) to your Pico's `CIRCUITPY` drive under the `lib` folder such that the library's `.mpy` files can be found under `/lib/adafruit_hid/`

4. Modify the `keybinds` and `pins` tuples in `code.py` with your key mappings and the pins that your keyswitches are attached to on your Pico.

5. Copy the modified `code.py` into the root of your Pico's `CIRCUITPY` drive.

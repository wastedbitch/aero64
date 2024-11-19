print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

# Enable layers module
layers = Layers()
keyboard.modules.append(layers)
keyboard.extensions.append(MediaKeys())

# Define layer keycodes
L1 = 0
L2 = 1

keyboard.col_pins = (board.GP27,board.GP28,board.GP29,board.GP24,board.GP25,board.GP14,board.GP15,board.GP3,board.GP5,board.GP6,board.GP9,board.GP10,board.GP11,board.GP12,board.GP13)
keyboard.row_pins = (board.GP20,board.GP1,board.GP0,board.GP6,board.GP2)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

def lock():
    return (
        KC.LGUI(KC.L),          # Win: Win + L
        KC.LCTL(KC.LCMD(KC.Q)), # mac: Ctrl + Cmd + Q
        KC.LCTL(KC.LALT(KC.L))  # Linux: Ctrl + Alt + L
    )

keyboard.keymap = [
    [
        KC.ESC,   KC.1,   KC.2,   KC.3,   KC.4,   KC.5,   KC.6,   KC.7,   KC.8,   KC.9,   KC.0,      KC.MINUS,   KC.EQL,   KC.PGUP,   KC.PGDOWN,
        KC.TAB,   XXX,    KC.Q,   KC.W,   KC.E,   KC.R,   KC.T,   KC.Y,   KC.U,   KC.I,   KC.O,      KC.P,       KC.LBRC,  KC.RBRC,   KC.BSLS,
        KC.CAPS,  XXX,    KC.A,   KC.S,   KC.D,   KC.F,   KC.G,   KC.H,   KC.J,   KC.K,   KC.L,      KC.SCLN,    KC.QUOT,  XXX,       KC.ENT,
        KC.LSFT,  XXX,    KC.Z,   KC.X,   KC.C,   KC.V,   KC.B,   XXX,    KC.N,   KC.M,   KC.COMM,   KC.DOT,     KC.SLSH,  KC.UP,     KC.RSHIFT,
        KC.LCTL,  KC.LWIN,XXX,    KC.LALT,XXX,    KC.SPACE,XXX,   XXX,    XXX,    KC.BSPC,KC.MO(L2), XXX,        KC.LEFT,  KC.DOWN,   KC.RIGHT,
    ],
    [
        KC.ESC,   KC.F1,  KC.F2,  KC.F3,  KC.F4,  KC.F5,  KC.F6,  KC.F7,  KC.F8,  KC.F9,  KC.F10,    KC.F11,     KC.F12,   KC.BRIU,   KC.BRID,
        KC.TAB,   XXX,    KC.Q,   KC.W,   KC.E,   KC.R,   KC.T,   KC.Y,   KC.U,   KC.I,   KC.O,      KC.P,       KC.LBRC,  KC.RBRC,   KC.BSLS,
        KC.CAPS,  XXX,    KC.A,   KC.S,   KC.D,   KC.F,   KC.G,   KC.H,   KC.J,   KC.K,   lock(),    KC.SCLN,    KC.QUOT,  XXX,       KC.ENT,
        KC.LSFT,  XXX,    KC.Z,   KC.X,   KC.C,   KC.V,   KC.B,   XXX,    KC.N,   KC.M,   KC.COMM,   KC.DOT,     KC.SLSH,  KC.VOLU,   KC.RSHIFT,
        KC.LCTL,  KC.LWIN,XXX,    KC.LALT,XXX,    KC.MPLY,XXX,    XXX,    XXX,    KC.BSPC,KC.MO(L1), XXX,        KC.MPRV,  KC.VOLD,   KC.MNXT,
    ]
]

if __name__ == '__main__':
    keyboard.go()
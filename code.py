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

keyboard.col_pins = (board.A1, board.A2, board.A3, board.D24, board.D25, board.SCK, board.MOSI, board.SCL, board.D5, board.D6, board.D9, board.D10, board.D11, board.D12, board.D13)
keyboard.row_pins = (board.MISO, board.RX ,board.TX, board.D4, board.SDA)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

def lock():
	return (
		KC.LGUI(KC.L),          # Win: Win + L
		KC.LCTL(KC.LCMD(KC.Q)), # mac: Ctrl + Cmd + Q
		KC.LCTL(KC.LALT(KC.L))  # Linux: Ctrl + Alt + L
	)

keyboard.keymap = [
	[
		KC.ESC,		KC.N1,		KC.N2,	KC.N3,		KC.N4,	KC.N5,		KC.N6,	KC.N7,	KC.N8,	KC.N9,		KC.N0,		KC.MINUS,	KC.EQL,		KC.PGDOWN,	KC.UP,
		KC.TAB,		KC.X,		KC.Q,	KC.W,		KC.E,	KC.R,		KC.T,	KC.Y,	KC.U,	KC.I,		KC.O,		KC.P,		KC.LBRC,	KC.RBRC,	KC.BSLS,
		KC.CAPS,	KC.X,		KC.A,	KC.S,		KC.D,	KC.F,		KC.G,	KC.H,	KC.J,	KC.K,		KC.L,		KC.SCLN,	KC.QUOT,	KC.X,		KC.ENT,
		KC.LSFT,	KC.X,		KC.Z,	KC.X,		KC.C,	KC.V,		KC.B,	KC.X,	KC.N,	KC.M,		KC.COMM,	KC.DOT,		KC.SLSH,	KC.UP,		KC.RSHIFT,
		KC.LCTL,	KC.LWIN,	KC.X,	KC.LALT,	KC.X,	KC.SPACE,	KC.X,	KC.X,	KC.X,	KC.BSPC,	KC.MO(L2),	KC.X,		KC.LEFT,	KC.DOWN,	KC.RIGHT,
	],
	[
		KC.ESC,		KC.F1,		KC.F2,	KC.F3,		KC.F4,	KC.F5,		KC.F6,	KC.F7,	KC.F8,	KC.F9,		KC.F10,		KC.F11,		KC.F12,		KC.BRID,	KC.BRIU,
		KC.TAB,		KC.X,		KC.Q,	KC.W,		KC.E,	KC.R,		KC.T,	KC.Y,	KC.U,	KC.I,		KC.O,		KC.LGUI(KC.L),		KC.LBRC,	KC.RBRC,	KC.BSLS,
		KC.CAPS,	KC.X,		KC.A,	KC.S,		KC.D,	KC.F,		KC.G,	KC.H,	KC.J,	KC.K,		KC.LCTL(KC.LALT(KC.L)),		KC.SCLN,	KC.QUOT,	KC.X,		KC.ENT,
		KC.LSFT,	KC.X,		KC.Z,	KC.X,		KC.C,	KC.V,		KC.B,	KC.X,	KC.N,	KC.LCTL(KC.LCMD(KC.Q)),		KC.COMM,	KC.DOT,		KC.SLSH,	KC.VOLU,	KC.RSHIFT,
		KC.LCTL,	KC.LWIN,	KC.X,	KC.LALT,	KC.X,	KC.MPLY,	KC.X,	KC.X,	KC.X,	KC.BSPC,	KC.MO(L1),	KC.X,		KC.MPRV,	KC.VOLD,	KC.MNXT,
	]
]

if __name__ == '__main__':
    keyboard.go()

	
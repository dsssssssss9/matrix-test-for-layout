def on_button_pressed_a():
    for index in range(16):
        ledmatrix.set_led_color(index, index, LEDMatrix.rgb(0, 0, 128))
        basic.pause(500)
    index2 = 15
    while index2 > -1:
        ledmatrix.set_led_color(15, index2, LEDMatrix.rgb(0, 0, 128))
        basic.pause(500)
        index2 -= 1
    for index3 in range(16):
        ledmatrix.set_led_color(index3, 15, LEDMatrix.rgb(0, 0, 128))
        basic.pause(500)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    ledmatrix.clear()
input.on_button_pressed(Button.B, on_button_pressed_b)

ledmatrix: LEDMatrix.LEDMatrix = None
basic.show_icon(IconNames.HEART)
ledmatrix = LEDMatrix.create(DigitalPin.P0, 16, 16, LEDColorMode.GRB)
ledmatrix.set_matrix_layout(FirstLEDPosition.TOP_RIGHT,
    LEDDirection.HORIZONTAL,
    LEDRowSetup.ZIG_ZAG)

def on_forever():
    pass
basic.forever(on_forever)

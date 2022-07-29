input.onButtonPressed(Button.A, function () {
    for (let index = 0; index <= 15; index++) {
        ledmatrix.setLEDColor(index, index, LEDMatrix.rgb(0, 0, 128))
        basic.pause(500)
    }
    index2 = 15
    while (index2 > -1) {
        ledmatrix.setLEDColor(15, index2, LEDMatrix.rgb(0, 0, 128))
        ledmatrix.setLEDColor(index2, 15, LEDMatrix.rgb(0, 0, 128))
        basic.pause(200)
        index2 += 0 - 1
    }
})
input.onButtonPressed(Button.B, function () {
    ledmatrix.clear()
})
let index2 = 0
let ledmatrix: LEDMatrix.LEDMatrix = null
basic.showIcon(IconNames.Heart)
ledmatrix = LEDMatrix.create(DigitalPin.P0, 16, 16, LEDColorMode.GRB)
ledmatrix.setMatrixLayout(FirstLEDPosition.topRight, LEDDirection.horizontal, LEDRowSetup.zigZag)
basic.forever(function () {
	
})

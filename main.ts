let TempC = 0
let TempF = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    TempC = input.temperature()
    basic.showNumber(TempC)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    TempF = TempC * 1.8 + 32
    basic.showNumber(TempF)
})

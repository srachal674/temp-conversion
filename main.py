TempC = 0
TempF = 0

def on_button_pressed_a():
    global TempC
    TempC = input.temperature()
    basic.show_number(TempC)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global TempF
    TempF = TempC * 1.8 + 32
    basic.show_number(TempF)
input.on_button_pressed(Button.B, on_button_pressed_b)

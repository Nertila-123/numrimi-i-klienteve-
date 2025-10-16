def on_button_pressed_a():
    basic.show_number(Numero_Klientet)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_logo_touched():
    global Numero_Klientet
    Numero_Klientet += 1
    basic.show_number(Numero_Klientet)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

Numero_Klientet = 0
Numero_Klientet = 0
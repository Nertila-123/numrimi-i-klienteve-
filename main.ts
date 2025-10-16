input.onButtonPressed(Button.A, function () {
    basic.showNumber(Numero_Klientet)
})
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    Numero_Klientet += 1
    basic.showNumber(Numero_Klientet)
})
let Numero_Klientet = 0
Numero_Klientet = 0

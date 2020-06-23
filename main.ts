let mazewall_distance = 0
let forward_distance = 0
let left_distance = 0
let right_distance = 0
let Forward = 0
let heading = 0
let Right = 0
let Left = 0
input.onButtonPressed(Button.A, function () {
    mazewall_distance = 15
    while (forward_distance > mazewall_distance && (left_distance > mazewall_distance && right_distance > mazewall_distance)) {
        Forward = input.compassHeading()
        if (Tinybit.Ultrasonic_Car() > mazewall_distance) {
            Tinybit.CarCtrlSpeed(Tinybit.CarState.Car_Run, 127)
        } else {
            Tinybit.CarCtrl(Tinybit.CarState.Car_Stop)
            forward_distance = Tinybit.Ultrasonic_Car()
        }
        if (heading != Right) {
            Tinybit.CarCtrl(Tinybit.CarState.Car_SpinRight)
        }
        right_distance = Tinybit.Ultrasonic_Car()
        if (heading != Left) {
            Tinybit.CarCtrl(Tinybit.CarState.Car_SpinLeft)
        }
        left_distance = Tinybit.Ultrasonic_Car()
        if (right_distance > left_distance) {
            if (heading != Right) {
                Tinybit.CarCtrl(Tinybit.CarState.Car_SpinRight)
            }
        }
    }
})
input.onButtonPressed(Button.AB, function () {
    for (let index = 0; index < 3; index++) {
        Tinybit.Music_Car(Tinybit.enMusic.nyan)
        Tinybit.RGB_Car_Big2(10, 20, 30)
        Tinybit.CarCtrlSpeed2(Tinybit.CarState.Car_Run, 130, -130)
        basic.pause(100)
        Tinybit.CarCtrlSpeed2(Tinybit.CarState.Car_Run, -130, 130)
    }
})
input.onButtonPressed(Button.B, function () {
    while (0 == 0) {
        heading = input.compassHeading()
    }
})
basic.forever(function () {
    if (Forward >= 270) {
        Right = Forward - 270
    } else {
        Right = Forward + 90
    }
})
basic.forever(function () {
    if (Forward <= 90) {
        Left = Forward + 270
    } else {
        Left = Forward - 90
    }
})

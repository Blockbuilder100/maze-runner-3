mazewall_distance = 0
forward_distance = 0
left_distance = 0
right_distance = 0
Forward = 0
heading = 0
Right = 0
Left = 0

def on_button_pressed_a():
    global mazewall_distance, Forward, forward_distance, right_distance, left_distance
    mazewall_distance = 15
    while forward_distance > mazewall_distance and (left_distance > mazewall_distance and right_distance > mazewall_distance):
        Forward = input.compass_heading()
        if Tinybit.Ultrasonic_Car() > mazewall_distance:
            Tinybit.car_ctrl_speed(Tinybit.CarState.CAR_RUN, 127)
        else:
            Tinybit.car_ctrl(Tinybit.CarState.CAR_STOP)
            forward_distance = Tinybit.Ultrasonic_Car()
        if heading != Right:
            Tinybit.car_ctrl(Tinybit.CarState.CAR_SPINRIGHT)
        right_distance = Tinybit.Ultrasonic_Car()
        if heading != Left:
            Tinybit.car_ctrl(Tinybit.CarState.CAR_SPINLEFT)
        left_distance = Tinybit.Ultrasonic_Car()
        if right_distance > left_distance:
            if heading != Right:
                Tinybit.car_ctrl(Tinybit.CarState.CAR_SPINRIGHT)
    for index in range(3):
        Tinybit.Music_Car(Tinybit.enMusic.NYAN)
        Tinybit.RGB_Car_Big2(10, 20, 30)
        Tinybit.car_ctrl_speed2(Tinybit.CarState.CAR_RUN, 130, -130)
        basic.pause(100)
        Tinybit.car_ctrl_speed2(Tinybit.CarState.CAR_RUN, -130, 130)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global heading
    while 0 == 0:
        heading = input.compass_heading()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    global Left
    if Forward <= 90:
        Left = Forward + 270
    else:
        Left = Forward - 90
basic.forever(on_forever)

def on_forever2():
    global Right
    if Forward >= 270:
        Right = Forward - 270
    else:
        Right = Forward + 90
basic.forever(on_forever2)

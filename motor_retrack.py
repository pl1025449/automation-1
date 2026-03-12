from motor_steering import set_motor_speeds

MAX_SPEED = 70
SPIN_SPEED = 40

def calc_motor_values(theta):
    p = theta / 180.0
    other_p = 1 - p
    left = int(p * MAX_SPEED)
    right = int(other_p * MAX_SPEED)
    return left, right

def follow_line(theta, line_found):
    if line_found:
        left, right = calc_motor_values(theta)
        set_left_motor(left)
        set_right_motor(right)
    else:
        # spin until center line is detected again
        MotorRun(0, forward, SPIN_SPEED)
        MotorRun(1, backward, SPIN_SPEED)

while True:
    theta, line_found = get_vision_result()  
    follow_line(theta, line_found)

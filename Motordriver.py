"""
Purpose:
Control the motor driver.

Pseudocode:
1. Define direction constants.
2. Try to import pi_client if available.
3. If pi_client is not available, fall back to printing commands.
4. Provide MotorRun() for individual motor control requests.
5. Provide helper functions for stop and basic movement.
"""
import pi_client
try:
    import pi_client
except ImportError:
    pi_client = None


# Direction constants
forward = "forward"
backward = "backward"
left = "left"
right = "right"
stop = "stop"


def _send_command(command: str) -> None:
    """
    Send a command to the robot.
    """
    if pi_client is not None:
        pi_client.execute_command(command)
    else:
        print(f"[Motordriver placeholder] Command sent: {command}")


def MotorRun(motor_index: int, direction: str, speed: int) -> None:
    """
    Run motor request.

    Parameters:
        motor_index (int): Which motor is being addressed.
        direction (str): Movement direction.
        speed (int): PWM speed value from 0 to 255.

    Returns: none
    """
    speed = max(0, min(255, int(speed)))

    if pi_client is not None:
        # Temporary simple mapping until the real pi_client interface is confirmed.
        # This can be replaced tomorrow without changing other files.
        _send_command(direction)
    else:
        print(
            f"[Motordriver placeholder] motor={motor_index}, "
            f"direction={direction}, speed={speed}"
        )


def stop_all() -> None:
    """
    Stop all robot motion.
    """
    _send_command(stop)


def move_forward(speed: int = 120) -> None:
    """
    Move the robot forward using both motors.
    """
    MotorRun(0, forward, speed)
    MotorRun(1, forward, speed)


def move_backward(speed: int = 120) -> None:
    """
    Move the robot backward using both motors.
    """
    MotorRun(0, backward, speed)
    MotorRun(1, backward, speed)


def turn_left(speed: int = 120) -> None:
    """
    Turn the robot left.
    """
    MotorRun(0, left, speed)
    MotorRun(1, left, speed)

def turn_right(speed: int = 120) -> None:
    """
    Turn the robot right.
    """
    MotorRun(0, right, speed)
    MotorRun(1, right, speed)

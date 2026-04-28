"""
Purpose:
Control the robot's automatic movement.

Pseudocode:
1. Check whether auto mode is running.
2. Check whether a stop line has already been detected.
3. Receive the newest camera frame from the server layer.
4. Process the frame using OpenCV.
5. Use the steering value to control motor speeds.
6. If the horizontal stop line is detected, wait a few seconds so the robot
   can pass over the line, then stop the robot.
7. Allow the GUI Play/Stop buttons to start and stop automation.
"""

import time
import processing_parallel
from processing_parallel import process_frame
from motor_steering import set_motor_speeds
from Motordriver import stop_all


# Auto-mode state variables
auto_running = False
stop_line_seen = False
stop_time = None

# How long the robot should keep moving after it detects the horizontal tape
# before stopping. You can tune this later if needed.
STOP_DELAY_SECONDS = 2.0


def start_automation():
    """
    Turn on automatic line-following mode.
    """
    global auto_running, stop_line_seen, stop_time

    auto_running = True
    stop_line_seen = False
    stop_time = None


def stop_automation():
    """
    Turn off automatic line-following mode and stop the robot.
    """
    global auto_running, stop_line_seen, stop_time

    auto_running = False
    stop_line_seen = False
    stop_time = None
    stop_all()
def is_running():
    """
    Return whether automatic mode is currently active.
    """
    return auto_running


def update_automation(frame):
    """
    Process one frame of video and update robot behavior.

    Parameters:
        frame: The newest camera frame.

    Returns:
        out: The processed overlay image.
    """
    global auto_running, stop_line_seen, stop_time

    # Always process the frame so the processed stream can still display overlays
    out, steering_value, stop_line_detected, center_line,left,right = process_frame(frame)

    if not auto_running:
        return out

    # If the stop line is detected for the first time, start the stop timer
    if stop_line_detected and not stop_line_seen:
        stop_line_seen = True
        stop_time = time.time()

    # If the robot has already seen the stop line, keep going for a short delay,
    # then stop completely
    if stop_line_seen:
        elapsed = time.time() - stop_time
        time.sleep(6.0)
        if elapsed >= STOP_DELAY_SECONDS:
            stop_automation()
            return out
    if center_line:
    # Normal line-following behavior
        _send_command('forward')
    elif left:
        set_motor_speeds(5.0)
    elif right:
        set_motor_speeds(-5.0)
    else:
       stop_automation()
    return out

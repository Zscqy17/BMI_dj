import threading
from xarm.wrapper import XArmAPI

def main():
    ip = me.parent().fetch('ip')
    data = me.parent().fetch('data')
    start_xarm(ip, data)

def start_xarm(ip, data):
    xarm_thread = threading.Thread(target=execute_movement, args=(ip, data))
    xarm_thread.start()

def execute_movement(ip, data): 
    print(data)
    arm = XArmAPI(ip, is_radian=True)
    arm.motion_enable(True)
    arm.set_mode(0)
    arm.set_state(0)
    arm.set_servo_angle(angle=data, speed=50, is_radian=False, wait=True)
    arm.disconnect()

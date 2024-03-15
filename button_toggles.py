
# Library imports
from vex import * # Important because it allows us to use vex commands like .spin and .position

# This is called robot configuration, where we configure our robot's devices.

brain = Brain()
controller_1 = Controller(PRIMARY) # Configuring controller

# Here, we are telling which motors are connected to which ports and cartridges
# so that the brain knows what to do when a motor is called.

# e.g. if we write in the code to spin the leftFrontMotor, the brain will know which
# one it is because we wrote what port it was located
#                                |
#                                |
#                                v
left_front_motor = Motor(Ports.PORT1, GearSetting.RATIO_6_1, False) # GearSetting is basically the gear cartridge.
left_rear_motor = Motor(Ports.PORT2, GearSetting.RATIO_6_1, False)
right_front_motor = Motor(Ports.PORT3, GearSetting.RATIO_6_1, True) # Reverse motors to drive both motors forward
right_rear_motor = Motor(Ports.PORT4, GearSetting.RATIO_6_1, True) # Reverse motors to drive both motors forward

left_drive = MotorGroup(left_front_motor, left_rear_motor)
right_drive = MotorGroup(right_front_motor, right_rear_motor)

random_motor = Motor(Ports.PORT5, GearSetting.RATIO_6_1, True)

def pre_auton():
    # This is the pre-auton phase, where you can clear motors, 
    # reset their positions, start things you need for the game.
    pass # Use a pass keyword when you are not doing anything in a function.

def autonomous():
    # Put anything related to auton under 'autonomous'.
    pass

def user_control():
    # Put anything related to driver control under 'user control'.
    # or it probably won't work the way its supposed to.
    while 1: # Forever loop
        # You want to put anything related to driver control and checking buttons in this loop.

        # Here, you could put driver control code.

        wait(20, MSEC) # The loop resets every 20 milliseconds

is_spinning = False # Toggle boolean; important for the toggles to work.
                    # A boolean is a variable that can store two values - true or false.

# The 'def' keyword means that you are defining a function, one of the most important aspects in coding.
# A function can perform any action you want; you just have to code it.

def buttonL1_macro():
  global active
  if is_spinning:
    is_spinning = False
    random_motor.stop(COAST) # can switch between BRAKE, HOLD, or COAST
  else:
    is_spinning = True
    random_motor.spin(FORWARD, 11, VOLT) # Spins motor in the forward direction

def buttonA_callback():
  global active
  if is_spinning:
    is_spinning = False
    random_motor.stop(COAST) # can switch between BRAKE, HOLD, or COAST
  else:
    is_spinning = True
    random_motor.spin(REVERSE, 11, VOLT) # Spins motor in the reverse direction

# Controller button callbacks/functions
controller.buttonL1.pressed(buttonL1_callback) # This is to spin randomMotor forward
controller.buttonA.pressed(buttonA_callback) # This is to spin randomMotor reverse

# You can make as many controller callbacks as possible for the different buttons on your controller.
# Just use the same layout for each of the functions.

# Here, you are stating that you want to run the user_control and 
# autonomous functions during a competition
comp = Competition(user_control, autonomous) # This is important, bc it tells the robot
# what to do during auton and driver control

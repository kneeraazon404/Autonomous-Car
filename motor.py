from serial import Serial
import time
import sys

print(sys.version)

direction = 1

ser = Serial("", 9600, timeout=1)


def driveMotor(speed, direction):
    enA = speed


if direction == 1:
    in1 = 1
    in2 = 0

elif direction == -1:
    in1 = 0
    in2 = 1

else:
    in1 = 0
    in2 = 0

valList = str(enA) + "," + str(in1) + "," + str(in2)
serString = ",".join(valList)
ser.write(serString)
time.sleep(0.1)

while motSpeed < 256:
    driveMotor(motSpeed, direction)
    motSpeed += 1
while motSpeed > 0:
    driveMotor(motSpeed, direction)
    motSpeed -= 1

    direction = -direction

"""Use this protocol to test for additional python functionality, namely the use of additional GUI prompts for
    loading information.  Also use to check the ability of this to cause pause/resume cycles."""

from opentrons import instruments, containers, robot
from PyQt5 import Qt, QtCore, QtGui, QtWidgets

# This Class is to check for interesting functionality that can be programmed
class Sample(QtWidgets.QDialog):
    def __init__(self):
        super(Sample).__init()
        QtWidgets.QPushButton("Hello")


# This loading of information is simply to check to see if the robot will do anything in between programs
p1000rack = containers.load('tiprack-1000ul', 'C2')
trash = containers.load('point', 'D1')

plate1 = containers.load('96-PCR-flat', 'A2')
plate2 = containers.load('96-PCR-flat', 'A1')

# Initialization of the sample test class
S = Sample()
S.

p1000_single = instruments.Pipette(
    axis="b",
    name='p1000',
    max_volume=1000,
    min_volume=100,
    channels=1,
    trash_container=trash,
    tip_racks=[p1000rack]
)

for well in range(0,10):
    p1000_single.transfer(500, plate1.wells(well), plate2.wells(well))

for command in robot.commands():
    print(command)


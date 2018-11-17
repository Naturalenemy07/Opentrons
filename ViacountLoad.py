"""This protocol is used to load the Viacount reagent into a 96 well plate."""

from opentrons import robot, containers, instruments

rack1 = containers.load('tiprack-1000ul', 'A1')

Viacount = containers.load('point', 'C2')  # Place in bottom right corner
viaplate = containers.load('96-PCR-flat', 'B1')
trash = containers.load('point','E1')

p1000_single = instruments.Pipette(
    axis="b",
    name='p1000single',
    max_volume=1000,
    min_volume=100,
    channels=1,
    tip_racks=[rack1],
    trash_container=trash
)
# Distribute reagent
p1000_single.distribute(90,Viacount,viaplate.wells())

for c in robot.commands():
    print(c)

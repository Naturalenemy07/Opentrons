"""This protocol is used pushing out the water from an autoclave run after the tips have been sterilized."""

from opentrons import robot, containers, instruments
import time

rack1 = containers.load('tiprack-200ul', 'A2')

water_dump = containers.load('point', 'B2')

p50_multi = instruments.Pipette(
    axis="a",
    name='p50multi',
    max_volume=50,
    min_volume=5,
    channels=8,
    tip_racks=rack1
)

# Take samples from all the rows of the Duetz plate and put them in the microplate
for i in range(0, 96, 8):  # This indexing is needed for the multichannel pipette
    p50_multi.aspirate(40)
    p50_multi.move_to(rack1.wells(i))
    p50_multi.blow_out(water_dump)
    p50_multi.move_to(rack1.wells(i).top(3))

for c in robot.commands():
    print(c)

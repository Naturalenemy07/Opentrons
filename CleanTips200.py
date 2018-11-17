"""This protocol is used for cleaning tiprack-200ul tips. It should normally be used with the p50 pipette as this
    offers a significant savings in time. You should have a dirty rack, clean rack (destination) and some cleaning
    fluid, usually 70% ethanol."""

from opentrons import robot, containers, instruments
import time

rack1 = containers.load('tiprack-200ul', 'A2')
rack2 = containers.load('tiprack-200ul', 'A1')
rack3 = containers.load('tiprack-200ul', 'C1')
racks = [rack1,rack2,rack3]

cleaning_solution = containers.load('point', 'C2')
millipore_water = containers.load('point', 'B2')

p50_multi = instruments.Pipette(
    axis="a",
    name='p50multi',
    max_volume=50,
    min_volume=5,
    channels=8,
    tip_racks= racks
)

# Take samples from all the rows of the Duetz plate and put them in the microplate
for cur_rack in racks:
    for i in range(0, 96, 8):  # This indexing is needed for the multichannel pipette
        p50_multi.pick_up_tip(cur_rack.wells(i))
        p50_multi.aspirate(40, cleaning_solution)
        p50_multi.mix(3, cleaning_solution)
        p50_multi.blow_out(cleaning_solution)
        p50_multi.aspirate(40, millipore_water)
        p50_multi.mix(5, millipore_water)
        p50_multi.blow_out(millipore_water)
        p50_multi.return_tip()

for c in robot.commands():
    print(c)

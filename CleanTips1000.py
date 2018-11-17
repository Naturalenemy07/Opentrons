"""This protocol is used for cleaning tiprack-1000ul tips. It should normally be used with the p50 pipette as this
    offers a significant savings in time. You should have a dirty rack, clean rack (destination) and some cleaning
    fluid, usually 70% ethanol."""

from opentrons import robot, containers, instruments

rack1 = containers.load('tiprack-1000ul', 'B2')
rack2 = containers.load('tiprack-1000ul', 'A2')
racks = [rack1,rack2]

cleaning_solution = containers.load('point', 'D2')

p1000_single = instruments.Pipette(
    axis="b",
    name='p1000single',
    max_volume=900,
    min_volume=100,
    channels=1,
    tip_racks=racks
)

# Pick up every tip and clean it with ethanol/whatever cleaning solution you desire
for cur_rack in racks:
    for i in range(0, 96):
        p1000_single.pick_up_tip(cur_rack.wells(i))
        #for j in range(2):
            #p1000_single.aspirate(600, cleaning_solution)
            #p1000_single.dispense(600, cleaning_solution)
        p1000_single.blow_out(cleaning_solution)
        p1000_single.return_tip()
    robot.pause()

for c in robot.commands():
    print(c)

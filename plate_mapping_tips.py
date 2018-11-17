from opentrons import robot, containers, instruments

# This protocol is a test for the p1000 to make sure the robot runs correctly on axis b

p1000rack = containers.load('tiprack-1000ul', 'C2')
trash = containers.load('point', 'D1')

plate1 = containers.load('96-PCR-flat', 'A2')
plate2 = containers.load('96-PCR-flat', 'A1')

p1000_single = instruments.Pipette(
    axis="b",
    name='p1000',
    max_volume=1000,
    min_volume=100,
    channels=1,
    trash_container=trash,
    tip_racks=[p1000rack]
)

# Run of protocol
for i in range(50,91):
	p1000_single.pick_up_tip(p1000rack.wells(i))
	p1000_single.transfer(300,plate1.wells(i),plate2.wells(i),new_tip='never')
	p1000_single.drop_tip(p1000rack.wells(i))

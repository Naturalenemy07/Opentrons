from opentrons import robot, instruments, containers

# Test to see if you can pause the robot from the code and then click to resume its functionality

p200rack = containers.load('tiprack-200ul', 'E2')
trash200 = containers.load('point', 'E1')

Duetz_plate = containers.load('96-deep-well', 'C1')
guava_plate = containers.load('96-PCR-flat', 'A1')

p50_multi = instruments.Pipette(
    axis="a",
    name='p50multi',
    max_volume=50,
    min_volume=5,
    channels=8,
    trash_container=trash200,
    tip_racks=[p200rack]
)

for i in range(0, 48, 8):  # This indexing is needed for the multichannel pipette
    p50_multi.distribute(30,Duetz_plate.wells(i),guava_plate.wells(i))

robot.pause()

for i in range(48,96,8):
    p50_multi.distribute(30,Duetz_plate.wells(i),guava_plate.wells(i))

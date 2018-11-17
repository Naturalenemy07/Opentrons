"""This protocol is for taking a Duetz measurement for flow cytometry and OD.  Current functionality allows you
    to pipette a given volume of sample for OD measurement and a given volume for flow cytometry.  Variable volumes
    and volumes connected to the OD reading will be featured in a forthcoming version of this protocol."""

"""THIS PROTOCOL ONLY MEASURES 1 DUETZ PLATE AT A TIME"""

from opentrons import robot, containers, instruments


p200rack = containers.load('tiprack-200ul', 'A2')
p200dirty = containers.load('tiprack-200ul', 'C2')
trash200 = containers.load('point', 'B2')

Duetz_plate = containers.load('96-deep-well', 'C1')
microplate = containers.load('384-plate', 'A1')
water_plate = containers.load('trough-12row', 'B1')


p50_multi = instruments.Pipette(
    axis="a",
    name='p50multi',
    max_volume=50,
    min_volume=5,
    channels=8,
    tip_racks=[p200rack]
)

# SET DILUTION FACTOR HERE
DILUTION_FACTOR = 2


# DILUTION ALGORITHM
# Prevents the sample and water from being greater than 50 ul
sample = 20
if DILUTION_FACTOR > 2:
    sample = 49.99/DILUTION_FACTOR
water = sample*(DILUTION_FACTOR-1)

dummy_list = ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12']
# Take samples from all the rows of the Duetz plate and put them in the guava plate first, then in the microplate
# Putting them in the plates simultaneously saves tips
# There is an option to put put them in separate loops allowing one to take the microplate out while it is sampling for
# the guava but we will investigate this on another growth study (not at night).
for i in range(0, 96, 8):  # This indexing is needed for the multichannel pipette
    p50_multi.pick_up_tip(p200rack.wells(i))
    p50_multi.aspirate(sample, Duetz_plate.wells(i))
    p50_multi.aspirate(water, water_plate.wells(dummy_list[int(i/8)]))
    p50_multi.dispense(sample+water, microplate.wells(i*2))
    p50_multi.blow_out()
    p50_multi.drop_tip(p200dirty.wells(i))


robot.home()

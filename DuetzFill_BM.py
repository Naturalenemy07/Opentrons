"""This protocol is for prepping different media conditions in a Duetz plate. This is a specialized protocol for
    the ViPaRe project and is preset for Saccharomyces cerevisiae media conditions."""

from opentrons import robot, containers, instruments


# Initializing the containers and media
p1000rack = containers.load('tiprack-1000ul', 'D2')
trash = containers.load('point', 'D1')

DuetzPlate = containers.load('96-deep-well', 'C1')
bigtubes = containers.load('tube-rack-15_50ml', 'A1')

# Medias
# SC-Leu-Ura: Bigtubes well A4
# Galactose: Bigtubes well B4
# Glucose: Bigtubes well B3
# Water: Bigtubes well A3
# G418: Bigtubes well A1
# Amp: Bigtubes well B1

# Initialize the Pipette
p1000_single = instruments.Pipette(
    axis="b",
    name='p1000',
    max_volume=1000,
    min_volume=50,
    channels=1,
    trash_container=trash,
    tip_racks=[p1000rack],
    dispense_speed=300
)

# ---PROTOCOL--- #
p1000_single.pick_up_tip()
p1000_single.distribute(250, bigtubes.wells('A4'), DuetzPlate.wells(), blow_out=False)
p1000_single.drop_tip()

"""for c in robot.commands():
    print(c)"""


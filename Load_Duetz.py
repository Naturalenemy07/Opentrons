"""This protocol is desinged to load 0.5mL from a 15mL falcon tube into the desired row(s) and column(s) of a 96well duetz plate.
 Place 15mL falcon tubes in C2 and the 96well duetz plate in C1 with single channel pipette on axis b."""


from opentrons import robot, containers, instruments

alphabet = "ABCDEFGHIJKLMNOP"

# Initialize the duetz plates and 15mL falcon tubes
Duetz_plate = containers.load('96-deep-well', 'C1')
bigtuberack = containers.load('tube-rack-15_50ml', 'B1')

# Initialize where the falcon tubes are going
falcon_tubes = 44
#falcon_tubes = ['poop', 'poopie', 'poopiepoop', 'mypoop', 'ghostpoop']
# Initialize trash and pipettes
trash = containers.load('point', 'C2')
p1000rack = containers.load('tiprack-1000ul', 'B2')

# Initialize the Pipette
p1000_single = instruments.Pipette(
    axis="b",
    name='p1000',
    max_volume=900,
    min_volume=50,
    channels=1,
    trash_container=trash,
    tip_racks=[p1000rack]
)

# ---Select Filling Orientation--- #
orient_matrix = {'row':12 , 'column':8 , 'doublerow':12 , 'doublecolumn':8}
orientation = 'column'
# ---Protocol--- #
count_limit = orient_matrix[orientation]
count = 1
#This will change if changed from number to list
for i in range(falcon_tubes):
    #if falcon_tubes.index(tube) % 2 == 0:
    if i % 2 == 0:
        cur_tube = 'C1'
    else:
        cur_tube = 'C2'
    if orientation == 'row':
        cur_wells = str(count)
        p1000_single.distribute(500, bigtuberack.wells(cur_tube), Duetz_plate.rows(cur_wells))
    elif orientation == 'column':
        cur_wells = alphabet[count-1]
        p1000_single.distribute(500, bigtuberack.wells(cur_tube), Duetz_plate.cols(cur_wells))
    elif orientation == 'doublerow':
        # need to combine into a list of two rows
        cur_wells = [str(count), str(count+1)]
        p1000_single.distribute(500, bigtuberack.wells(cur_tube), Duetz_plate.rows(cur_wells))
        # additional iteration because of the double rows
        count += 1
    elif orientation == 'doublecolumn':
        # need to combine into a list of two columns
        cur_wells = [alphabet[count-1], alphabet[count]]
        p1000_single.distribute(500, bigtuberack.wells(cur_tube), Duetz_plate.cols(cur_wells))
        # additional iteration because of the double columns
    count += 1
    if cur_tube == 'C2':
        robot.pause()
    if count > count_limit:
        robot.pause()
        robot.comment("Load a new Duetz plate.")
        count = 1

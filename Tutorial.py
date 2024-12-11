# Environment setup
from opentrons import protocol_api

# Define metadata
metadata = {
    'protocolName': 'Tutorial',
    'author': 'Christian Potts <christian.potts@maine.edu>',
    'description': 'Introductory protocol to familiarize myself with the OT2',
}

# requirements
requirements = {
    'robotType': 'OT-2',
    'apiLevel': '2.20'
}

def run(protocol: protocol_api.ProtocolContext):
    # Labware
    plate = protocol.load_labware(
        "corning_96_wellplate_360ul_flat", location="1"
    )
    tiprack = protocol.load_labware(
        "opentrons_96_tiprack_300ul", location="2"
    )

    # Pipettes
    left_pipette = protocol.load_instrument(
        "p300_single", 
        mount="left",
        tip_racks=[tiprack]
    )

    right_pipette = protocol.load_instrument(
        "p50_single",
        mount="right",
        tip_racks=[tiprack]
    )

    ## Commands
    # 30uL, p300
    left_pipette.pick_up_tip()
    left_pipette.aspirate(30, plate["A1"])
    left_pipette.dispense(30, plate["B1"])
    left_pipette.drop_tip()

    # 150uL, p300
    left_pipette.pick_up_tip()
    left_pipette.aspirate(150, plate["A1"])
    left_pipette.dispense(150, plate["C1"])
    left_pipette.drop_tip()

    # 300uL, p300
    left_pipette.pick_up_tip()
    left_pipette.aspirate(300, plate["A2"])
    left_pipette.dispense(300, plate["B2"])
    left_pipette.drop_tip()

    # 5uL, p50
    left_pipette.pick_up_tip()
    left_pipette.aspirate(30, plate["A3"])
    left_pipette.dispense(30, plate["B3"])
    left_pipette.drop_tip()

    # 25uL, p50
    left_pipette.pick_up_tip()
    left_pipette.aspirate(25, plate["A3"])
    left_pipette.dispense(25, plate["C3"])
    left_pipette.drop_tip()

    # 50uL, p50
    left_pipette.pick_up_tip()
    left_pipette.aspirate(50, plate["A2"])
    left_pipette.dispense(50, plate["D3"])
    left_pipette.drop_tip()
"""Global Constants"""
# Standard
import logging

# Third Party
import numpy as np

# Local

# -------------------------------------------------------------------------------------------------
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
# -------------------------------------------------------------------------------------------------

CUMULATIVE_ROUND_CASH = np.array(
    [
        0,
        121,
        258,
        396,
        571,
        735,
        898,
        1080,
        1280,
        1479,
        1793,
        1982,
        2174,
        2456,
        2715,
        2981,
        3249,
        3414,
        3772,
        4032,
        4218,
        4569,
        4867,
        5144,
        5311,
        5646,
        5979,
        6641,
        6907,
        7296,
        7633,
        8170,
        8797,
        9002,
        9914,
        11064,
        11960,
        13299,
        14576,
        16335,
        16856,
        19037,
        19696,
        20974,
        22268,
        24690,
        25406,
        27043,
        29886,
        34644,
        37660,
        38683,
        40202,
        41050,
        43171,
        45576,
        46785,
        48565,
        50784,
        52864,
        53706,
        54809,
        56066,
        58762,
        59480,
        62420,
        63291,
        64181,
        64825,
        66080,
        68563,
        69929,
        71296,
        72550,
        75455,
        77982,
        79157,
        81556,
        86276,
        92841,
        94098,
        99319,
        103930,
        108533,
        115430,
        117907,
        118688,
        121147,
        124292,
        126293,
        126461,
        130480,
        134845,
        136618,
        144110,
        147653,
        157432,
        158672,
        168148,
        170796,
        172151,
        172724,
        174983,
        180961,
        188359,
        192565,
        194347,
        198016,
        203822,
        211272,
        213760,
        223227,
        225106,
        228088,
        233493,
        238898,
        242842,
        243797,
        248040,
        250053,
        255097,
        256474,
        258340,
        260844,
        263136,
        265634,
        266393,
        267495,
        269092,
        271108,
        272667,
        274868,
        277825,
        281269,
        282494,
        284367,
        285835,
        289134,
        290099,
        292031,
        292570,
    ]
)

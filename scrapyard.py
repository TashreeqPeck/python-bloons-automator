"""Script to beat the scrapyard map on easy"""

import logging
from maps import Scrapyard
from constants import Difficulty, UpgradePath
from monkeys import DartMonkey, NinjaMonkey, SniperMonkey
from monkeys.heroes import Obyn
from bloons_driver import BloonsDriver

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

ui = BloonsDriver(Difficulty.EASY, Scrapyard())
hero = Obyn(Difficulty.EASY)
ninja = NinjaMonkey(Difficulty.EASY)
dart = DartMonkey(Difficulty.EASY)
sniper = SniperMonkey(Difficulty.EASY)

while not ui.game_ended():
    match (ui.round):
        case 1:
            ui.place_monkey(dart, (385, 188), True)
            ui.upgrade_monkey(dart, UpgradePath.TOP)
            ui.upgrade_monkey(dart, UpgradePath.MIDDLE)
            ui.upgrade_monkey(dart, UpgradePath.MIDDLE)
        case 6:
            ui.place_monkey(sniper, (1990, 1270), True)
        case 8:
            ui.upgrade_monkey(sniper, UpgradePath.TOP)
        case 10:
            ui.upgrade_monkey(sniper, UpgradePath.MIDDLE)
        case 13:
            ui.place_monkey(hero, (540, 1140), True)
        case 15:
            ui.place_monkey(ninja, (390, 300), True)
        case 16:
            ui.upgrade_monkey(ninja, UpgradePath.TOP)
        case 18:
            ui.upgrade_monkey(ninja, UpgradePath.BOTTOM)
        case 22:
            ui.upgrade_monkey(ninja, UpgradePath.TOP)
        case 24:
            ui.upgrade_monkey(ninja, UpgradePath.TOP)
        case 31:
            ui.upgrade_monkey(ninja, UpgradePath.TOP)
            ui.upgrade_monkey(ninja, UpgradePath.BOTTOM)
        case 32:
            ui.upgrade_monkey(dart, UpgradePath.TOP)
        case 33:
            ui.upgrade_monkey(dart, UpgradePath.MIDDLE)
        case 36:
            ui.upgrade_monkey(sniper, UpgradePath.MIDDLE)
            ui.upgrade_monkey(sniper, UpgradePath.TOP)
        case 40:
            ui.upgrade_monkey(sniper, UpgradePath.MIDDLE)

    ui.complete_round()

logger.info("Scrapyard Complete!")

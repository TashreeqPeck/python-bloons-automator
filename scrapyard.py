"""Script to beat the scrapyard map on easy"""

import logging
from maps import Scrapyard
from constants import Difficulty, UpgradePath
from monkeys.dart_monkey import DartMonkey
from monkeys.heroes.obyn import Obyn
from monkeys.ninja_monkey import NinjaMonkey
from monkeys.sniper_monkey import SniperMonkey
from bloons_driver import BloonsDriver

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

ui = BloonsDriver(Difficulty.EASY, Scrapyard())
hero = Obyn(Difficulty.EASY)
ninja = NinjaMonkey(Difficulty.EASY)
dart = DartMonkey(Difficulty.EASY)
sniper = SniperMonkey(Difficulty.EASY)

ui.place_monkey(dart, (385, 188), True)
ui.upgrade_monkey(dart, UpgradePath.TOP)
ui.upgrade_monkey(dart, UpgradePath.MIDDLE)
ui.upgrade_monkey(dart, UpgradePath.MIDDLE)

ui.complete_round()  # 1
ui.complete_round()  # 2
ui.complete_round()  # 3
ui.complete_round()  # 4
ui.complete_round()  # 5

ui.place_monkey(sniper, (1990, 1270), True)
ui.complete_round()  # 6
ui.complete_round()  # 7
ui.upgrade_monkey(sniper, UpgradePath.TOP)
ui.complete_round()  # 8
ui.complete_round()  # 9
ui.upgrade_monkey(sniper, UpgradePath.MIDDLE)
ui.complete_round()  # 10
ui.complete_round()  # 11
ui.complete_round()  # 12

ui.place_monkey(hero, (540, 1140), True)
ui.complete_round()  # 13
ui.complete_round()  # 14

ui.place_monkey(ninja, (390, 300), True)
ui.complete_round()  # 15
ui.upgrade_monkey(ninja, UpgradePath.TOP)
ui.complete_round()  # 16
ui.complete_round()  # 17
ui.upgrade_monkey(ninja, UpgradePath.BOTTOM)
ui.complete_round()  # 18
ui.complete_round()  # 19
ui.complete_round()  # 20
ui.complete_round()  # 21
ui.upgrade_monkey(ninja, UpgradePath.TOP)
ui.complete_round()  # 22
ui.complete_round()  # 23
ui.upgrade_monkey(ninja, UpgradePath.TOP)
ui.complete_round()  # 24
ui.complete_round()  # 25
ui.complete_round()  # 26
ui.complete_round()  # 27
ui.complete_round()  # 28
ui.complete_round()  # 29
ui.complete_round()  # 30
ui.upgrade_monkey(ninja, UpgradePath.TOP)
ui.upgrade_monkey(ninja, UpgradePath.BOTTOM)
ui.complete_round()  # 31

ui.upgrade_monkey(dart, UpgradePath.TOP)
ui.complete_round()  # 32
ui.upgrade_monkey(dart, UpgradePath.MIDDLE)
ui.complete_round()  # 33
ui.complete_round()  # 34
ui.complete_round()  # 35

ui.upgrade_monkey(sniper, UpgradePath.MIDDLE)
ui.upgrade_monkey(sniper, UpgradePath.TOP)
ui.complete_round()  # 36
ui.complete_round()  # 37
ui.complete_round()  # 38
ui.complete_round()  # 39
ui.upgrade_monkey(sniper, UpgradePath.MIDDLE)
ui.complete_round()  # 40

logger.info("Scrapyard Complete!")

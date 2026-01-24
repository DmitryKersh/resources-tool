from factories import *
import json

FACTORY_BRICKS = Factory('bricks', FACTORY_BRICK_CONTRACT, 359)
FACTORY_CONCRETE = Factory('concrete', FACTORY_CONCRETE_CONTRACT, 258, 1.7)
FACTORY_FUEL = Factory('fuel', FACTORY_FUEL_CONTRACT, 69, 1.5)
FACTORY_COPPER = Factory('copper', FACTORY_COPPER_CONTRACT, 58, 1.5)
FACTORY_ALUMINUM = Factory('aluminum', FACTORY_ALUMINUM_CONTRACT, 50, 1.5)
FACTORY_MEDTECH = Factory('medtech', FACTORY_MEDTECH_CONTRACT, 39, 1.7)
FACTORY_STEEL = Factory('steel', FACTORY_STEEL_CONTRACT, 57)
FACTORY_GLASS = Factory('glass', FACTORY_GLASS_CONTRACT, 48)
FACTORY_INSECTICIDE = Factory('insecticide', FACTORY_INSECTICIDE_CONTRACT, 25)
FACTORY_PLASTIC = Factory('plastic', FACTORY_PLASTIC_CONTRACT, 35)
FACTORY_LITHIUM = Factory('lithium', FACTORY_LITHIUM_CONTRACT, 27)
FACTORY_ACCUMULATOR = Factory('accumulator', FACTORY_ACCUMULATOR_CONTRACT, 16)
FACTORY_WEAPONS = Factory('weapons', FACTORY_WEAPONS_CONTRACT, 19)
FACTORY_SILICON = Factory('silicon', FACTORY_SILICON_CONTRACT, 11)
FACTORY_CIRCUITRY = Factory('circuitry', FACTORY_CIRCUITRY_CONTRACT, 15)
FACTORY_TITANIUM = Factory('titanium', FACTORY_TITANIUM_CONTRACT, 17)
FACTORY_SILVER = Factory('silver', FACTORY_SILVER_CONTRACT, 8)
FACTORY_GOLD = Factory('gold', FACTORY_GOLD_CONTRACT, 10)
FACTORY_FERTILIZER = Factory('fertilizer', FACTORY_FERTILIZER_CONTRACT, 39)
FACTORY_TRUCKS = Factory('trucks', FACTORY_TRUCKS_CONTRACT, 3)
FACTORY_DRONE = Factory('drone', FACTORY_DRONE_CONTRACT, 9)
FACTORY_JEWELLERY = Factory('jewellery', FACTORY_JEWELLERY_CONTRACT, 22)

FACTORIES = [
    FACTORY_BRICKS,
    FACTORY_CONCRETE,
    FACTORY_FERTILIZER,
    FACTORY_STEEL,
    FACTORY_FUEL,
    FACTORY_GLASS,
    FACTORY_COPPER,
    FACTORY_INSECTICIDE,
    FACTORY_ALUMINUM,
    FACTORY_PLASTIC,
    FACTORY_LITHIUM,
    FACTORY_ACCUMULATOR,
    FACTORY_WEAPONS,
    FACTORY_SILICON,
    FACTORY_CIRCUITRY,
    FACTORY_TITANIUM,
    FACTORY_MEDTECH,
    FACTORY_SILVER,
    FACTORY_GOLD,
    FACTORY_JEWELLERY,
    FACTORY_DRONE,
    FACTORY_TRUCKS,
]
hint = '''
1 = Топ N апов заводов с твоего лвл
2 = Лучшее соотношение с нуля за N апов
'''
try:
    config = json.load(open('config.json'))
    factory_config = config['factories']
    for factory in FACTORIES:
        if factory_config.get(factory.name) is not None:
            factory.lvl = factory_config[factory.name]['lvl']
            factory.speed_mult = factory_config[factory.name]['speed_mult']
    res_config = config['resources']
    for resource in RESOURCES:
        if res_config.get(resource.name) is not None:
            resource.price = res_config[resource.name]
except Exception as e:
    print("error reading config")


match input(hint):
    case '1':
        for s in topNforUpgrade(FACTORIES, int(input("Топ сколько показать?"))):
            print(s)
    case '2':
        for s in bestConfig(FACTORIES, int(input("Сколько апов?"))):
            print(s)
    case _:
        print("неизв. команда")
from classes import ResourceRequirement, FactoryUpgradeRequirement, FactoryContract
from res import RESOURCES

RESOURCE_BY_NAME = {resource.name: resource for resource in RESOURCES}


def rr(resource_name: str, amount: int) -> ResourceRequirement:
    return ResourceRequirement(RESOURCE_BY_NAME[resource_name], amount)


_FACTORY_DATA = {
    'CONCRETE': {
        'upgrade': [
            ('bricks', 1000),
            ('clay', 1000),
            ('limestone', 500),
            ('money', 2000000),
        ],
        'input': [
            ('limestone', 2),
            ('gravel', 3),
            ('money', 20),
        ],
        'output': ('concrete', 14),
        'hourspeed': 2100,
    },

    'BRICK': {
        'upgrade': [
            ('clay', 200),
            ('money', 500000),
        ],
        'input': [
            ('clay', 2),
            ('money', 10),
        ],
        'output': ('bricks', 2),
        'hourspeed': 800,
    },

    'FUEL': {
        'upgrade': [
            ('steel', 500),
            ('gravel', 500),
            ('concrete', 16000),
            ('money', 20000000),
        ],
        'input': [
            ('money', 150),
            ('crude_oil', 4),
        ],
        'output': ('fuel', 8),
        'hourspeed': 640,
    },

    'COPPER': {
        'upgrade': [
            ('steel', 1000),
            ('glass', 500),
            ('concrete', 25000),
            ('money', 40000000),
        ],
        'input': [
            ('money', 2500),
            ('copper_ore', 9),
        ],
        'output': ('copper', 3),
        'hourspeed': 270,
    },

    'ALUMINUM': {
        'upgrade': [
            ('steel', 2500),
            ('glass', 1500),
            ('concrete', 25000),
            ('money', 40000000),
        ],
        'input': [
            ('money', 5000),
            ('bauxite', 24),
        ],
        'output': ('aluminum', 4),
        'hourspeed': 320,
    },

    'MEDTECH': {
        'upgrade': [
            ('steel', 9500),
            ('plastic', 16000),
            ('concrete', 40000),
            ('money', 500000000),
        ],
        'input': [
            ('money', 90000),
            ('plastic', 2),
            ('circuitry', 2),
            ('titanium', 4),
        ],
        'output': ('medtech', 10),
        'hourspeed': 400,
    },

    'STEEL': {
        'upgrade': [
            ('bricks', 500),
            ('limestone', 3000),
            ('concrete', 9000),
            ('money', 10000000),
        ],
        'input': [
            ('money', 350),
            ('iron', 7),
            ('coal', 10),
        ],
        'output': ('steel', 1),
        'hourspeed': 450,
    },

    'GLASS': {
        'upgrade': [
            ('bricks', 3000),
            ('limestone', 150),
            ('concrete', 25000),
            ('money', 20000000),
        ],
        'input': [
            ('money', 3000),
            ('fuel', 8),
            ('limestone', 4),
            ('sand', 6),
        ],
        'output': ('glass', 8),
        'hourspeed': 640,
    },

    'INSECTICIDE': {
        'upgrade': [
            ('copper', 500),
            ('steel', 2000),
            ('concrete', 25000),
            ('money', 30000000),
        ],
        'input': [
            ('money', 2400),
            ('copper', 1),
            ('limestone', 3),
        ],
        'output': ('insecticide', 35),
        'hourspeed': 3500,
    },

    'PLASTIC': {
        'upgrade': [
            ('aluminum', 500),
            ('steel', 1000),
            ('concrete', 16000),
            ('money', 50000000),
        ],
        'input': [
            ('money', 400),
            ('crude_oil', 1),
        ],
        'output': ('plastic', 10),
        'hourspeed': 1800,
    },

    'LITHIUM': {
        'upgrade': [
            ('glass', 1000),
            ('steel', 10000),
            ('concrete', 25000),
            ('money', 60000000),
        ],
        'input': [
            ('money', 5000),
            ('lithium_ore', 115),
        ],
        'output': ('lithium', 5),
        'hourspeed': 750,
    },

    'ACCUMULATOR': {
        'upgrade': [
            ('aluminum', 10000),
            ('glass', 6000),
            ('concrete', 20000),
            ('money', 100000000),
        ],
        'input': [
            ('money', 75000),
            ('lithium', 20),
            ('aluminum', 10),
            ('plastic', 40),
        ],
        'output': ('accumulator', 10),
        'hourspeed': 600,
    },

    'WEAPONS': {
        'upgrade': [
            ('bricks', 500000),
            ('glass', 10000),
            ('concrete', 50000),
            ('money', 200000000),
        ],
        'input': [
            ('money', 250000),
            ('accumulator', 1),
            ('steel', 1),
            ('aluminum', 1),
        ],
        'output': ('weapons', 25),
        'hourspeed': 125,
    },

    'SILICON': {
        'upgrade': [
            ('glass', 1500),
            ('steel', 1200),
            ('concrete', 20000),
            ('money', 220000000),
        ],
        'input': [
            ('money', 49500),
            ('sand', 20),
            ('fuel', 5),
            ('clay', 1),
        ],
        'output': ('silicon', 2),
        'hourspeed': 120,
    },

    'CIRCUITRY': {
        'upgrade': [
            ('aluminum', 1000),
            ('glass', 8000),
            ('concrete', 20000),
            ('money', 300000000),
        ],
        'input': [
            ('money', 5000),
            ('plastic', 4),
            ('copper', 3),
            ('silicon', 1),
        ],
        'output': ('circuitry', 8),
        'hourspeed': 480,
    },

    'TITANIUM': {
        'upgrade': [
            ('glass', 2500),
            ('steel', 10000),
            ('concrete', 30000),
            ('money', 350000000),
        ],
        'input': [
            ('money', 10000),
            ('ilmenite', 8),
        ],
        'output': ('titanium', 4),
        'hourspeed': 320,
    },

    'SILVER': {
        'upgrade': [
            ('glass', 1500),
            ('steel', 15000),
            ('concrete', 35000),
            ('money', 750000000),
        ],
        'input': [
            ('money', 10000),
            ('silver_ore', 8),
        ],
        'output': ('silver', 50),
        'hourspeed': 3000,
    },

    'GOLD': {
        'upgrade': [
            ('glass', 20000),
            ('steel', 20000),
            ('concrete', 20000),
            ('money', 1000000000),
        ],
        'input': [
            ('money', 20000),
            ('gold_ore', 20),
        ],
        'output': ('gold', 3),
        'hourspeed': 240,
    },

    'FERTILIZER': {
        'upgrade': [
            ('bricks', 2500),
            ('limestone', 500),
            ('concrete', 5000),
            ('money', 4000000),
        ],
        'input': [
            ('money', 90),
            ('limestone', 8),
        ],
        'output': ('fertilizer', 11),
        'hourspeed': 1210,
    },

    'TRUCKS': {
        'upgrade': [
            ('bricks', 500000),
            ('circuitry', 90000),
            ('silver', 50000),
            ('money', 2000000000),
        ],
        'input': [
            ('money', 2500000),
            ('steel', 100),
            ('accumulator', 25),
            ('silver', 50),
        ],
        'output': ('trucks', 50),
        'hourspeed': 100,
    },

    'DRONE': {
        'upgrade': [
            ('glass', 40000),
            ('plastic', 120000),
            ('concrete', 80000),
            ('money', 2000000000),
        ],
        'input': [
            ('money', 25000000),
            ('titanium', 50),
            ('circuitry', 25),
            ('accumulator', 250),
        ],
        'output': ('drone', 1),
        'hourspeed': 1,
    },

    'JEWELLERY': {
        'upgrade': [
            ('bricks', 90000),
            ('glass', 20000),
            ('concrete', 20000),
            ('money', 500000000),
        ],
        'input': [
            ('money', 50000),
            ('diamond', 1000),
            ('silver', 1),
            ('gold', 1),
        ],
        'output': ('jewellery', 2),
        'hourspeed': 100,
    },
}


FACTORY_CONTRACTS = {}

for factory_name, data in _FACTORY_DATA.items():
    upgrade = FactoryUpgradeRequirement(
        [rr(resource_name, amount) for resource_name, amount in data['upgrade']]
    )

    inputs = [
        rr(resource_name, amount)
        for resource_name, amount in data['input']
    ]

    output = rr(*data['output'])

    contract = FactoryContract(
        upgrade_req=upgrade,
        req=inputs,
        output=output,
        hourspeed=data['hourspeed'],
    )

    globals()[f'FACTORY_{factory_name}_UP'] = upgrade
    globals()[f'FACTORY_{factory_name}_IN'] = inputs
    globals()[f'FACTORY_{factory_name}_OUT'] = output
    globals()[f'FACTORY_{factory_name}_CONTRACT'] = contract

    FACTORY_CONTRACTS[factory_name.lower()] = contract


__all__ = ['FACTORY_CONTRACTS'] + [
    f'FACTORY_{factory_name}_{suffix}'
    for factory_name in _FACTORY_DATA
    for suffix in ('UP', 'IN', 'OUT', 'CONTRACT')
]
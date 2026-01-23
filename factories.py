from res import *

# concrete
FACTORY_CONCRETE_UP = FactoryUpgradeRequirement([
    ResourceRequirement(RES_BRICKS, 1000),
    ResourceRequirement(RES_CLAY, 1000),
    ResourceRequirement(RES_LIMESTONE, 500),
    ResourceRequirement(RES_MONEY, 2000000),
])
FACTORY_CONCRETE_IN = [
    ResourceRequirement(RES_LIMESTONE, 2),
    ResourceRequirement(RES_GRAVEL, 3),
    ResourceRequirement(RES_MONEY, 20),
]
FACTORY_CONCRETE_OUT = ResourceRequirement(RES_CONCRETE, 14)
FACTORY_CONCRETE_CONTRACT = FactoryContract(FACTORY_CONCRETE_UP, FACTORY_CONCRETE_IN, FACTORY_CONCRETE_OUT, 2100)

# brick
FACTORY_BRICK_UP = FactoryUpgradeRequirement([
    ResourceRequirement(RES_CLAY, 200),
    ResourceRequirement(RES_MONEY, 500000),
])
FACTORY_BRICK_IN = [
    ResourceRequirement(RES_CLAY, 2),
    ResourceRequirement(RES_MONEY, 10),
]
FACTORY_BRICK_OUT = ResourceRequirement(RES_BRICKS, 2)
FACTORY_BRICK_CONTRACT = FactoryContract(FACTORY_BRICK_UP, FACTORY_BRICK_IN, FACTORY_BRICK_OUT, 800)

# fuel
FACTORY_FUEL_UP = FactoryUpgradeRequirement([
    ResourceRequirement(RES_STEEL, 500),
    ResourceRequirement(RES_GRAVEL, 500),
    ResourceRequirement(RES_CONCRETE, 16000),
    ResourceRequirement(RES_MONEY, 20000000),
])
FACTORY_FUEL_IN = [
    ResourceRequirement(RES_MONEY, 150),
    ResourceRequirement(RES_CRUDE_OIL, 4),
]
FACTORY_FUEL_OUT = ResourceRequirement(RES_FUEL, 8)
FACTORY_FUEL_CONTRACT = FactoryContract(FACTORY_FUEL_UP, FACTORY_FUEL_IN, FACTORY_FUEL_OUT, 640)

# copper
FACTORY_COPPER_UP = FactoryUpgradeRequirement([
    ResourceRequirement(RES_STEEL, 1000),
    ResourceRequirement(RES_GLASS, 500),
    ResourceRequirement(RES_CONCRETE, 25000),
    ResourceRequirement(RES_MONEY, 40000000),
])
FACTORY_COPPER_IN = [
    ResourceRequirement(RES_MONEY, 2500),
    ResourceRequirement(RES_COPPER_ORE, 9),
]
FACTORY_COPPER_OUT = ResourceRequirement(RES_COPPER, 3)
FACTORY_COPPER_CONTRACT = FactoryContract(FACTORY_COPPER_UP, FACTORY_COPPER_IN, FACTORY_COPPER_OUT, 270)

FACTORY_ALUMINUM_UP = FactoryUpgradeRequirement([
    ResourceRequirement(RES_STEEL, 2500),
    ResourceRequirement(RES_GLASS, 1500),
    ResourceRequirement(RES_CONCRETE, 25000),
    ResourceRequirement(RES_MONEY, 40000000),
])
FACTORY_ALUMINUM_IN = [
    ResourceRequirement(RES_MONEY, 5000),
    ResourceRequirement(RES_BAUXITE, 24),
]
FACTORY_ALUMINUM_OUT = ResourceRequirement(RES_ALUMINUM, 4)
FACTORY_ALUMINUM_CONTRACT = FactoryContract(FACTORY_ALUMINUM_UP, FACTORY_ALUMINUM_IN, FACTORY_ALUMINUM_OUT, 320)

FACTORY_MEDTECH_UP = FactoryUpgradeRequirement([
    ResourceRequirement(RES_STEEL, 9500),
    ResourceRequirement(RES_PLASTIC, 16000),
    ResourceRequirement(RES_CONCRETE, 40000),
    ResourceRequirement(RES_MONEY, 500000000),
])
FACTORY_MEDTECH_IN = [
    ResourceRequirement(RES_MONEY, 90000),
    ResourceRequirement(RES_PLASTIC, 2),
    ResourceRequirement(RES_CIRCUITRY, 2),
    ResourceRequirement(RES_TITANIUM, 4),
]
FACTORY_MEDTECH_OUT = ResourceRequirement(RES_MEDTECH, 10)
FACTORY_MEDTECH_CONTRACT = FactoryContract(FACTORY_MEDTECH_UP, FACTORY_MEDTECH_IN, FACTORY_MEDTECH_OUT, 460)

FACTORY_STEEL_UP = FactoryUpgradeRequirement([
    ResourceRequirement(RES_BRICKS, 500),
    ResourceRequirement(RES_LIMESTONE, 3000),
    ResourceRequirement(RES_CONCRETE, 9000),
    ResourceRequirement(RES_MONEY, 10000000),
])
FACTORY_STEEL_IN = [
    ResourceRequirement(RES_MONEY, 350),
    ResourceRequirement(RES_IRON, 7),
    ResourceRequirement(RES_COAL, 10),
]
FACTORY_STEEL_OUT = ResourceRequirement(RES_STEEL, 1)
FACTORY_STEEL_CONTRACT = FactoryContract(FACTORY_STEEL_UP, FACTORY_STEEL_IN, FACTORY_STEEL_OUT, 450)

FACTORY_GLASS_UP = FactoryUpgradeRequirement([
    ResourceRequirement(RES_BRICKS, 3000),
    ResourceRequirement(RES_LIMESTONE, 150),
    ResourceRequirement(RES_CONCRETE, 25000),
    ResourceRequirement(RES_MONEY, 20000000),
])
FACTORY_GLASS_IN = [
    ResourceRequirement(RES_MONEY, 3000),
    ResourceRequirement(RES_FUEL, 8),
    ResourceRequirement(RES_LIMESTONE, 4),
    ResourceRequirement(RES_SAND, 6),
]
FACTORY_GLASS_OUT = ResourceRequirement(RES_GLASS, 8)
FACTORY_GLASS_CONTRACT = FactoryContract(FACTORY_GLASS_UP, FACTORY_GLASS_IN, FACTORY_GLASS_OUT, 640)

FACTORY_INSECTICIDE_UP = FactoryUpgradeRequirement([
    ResourceRequirement(RES_COPPER, 500),
    ResourceRequirement(RES_STEEL, 2000),
    ResourceRequirement(RES_CONCRETE, 25000),
    ResourceRequirement(RES_MONEY, 30000000),
])
FACTORY_INSECTICIDE_IN = [
    ResourceRequirement(RES_MONEY, 2400),
    ResourceRequirement(RES_COPPER, 1),
    ResourceRequirement(RES_LIMESTONE, 3),
]
FACTORY_INSECTICIDE_OUT = ResourceRequirement(RES_INSECTICIDE, 35)
FACTORY_INSECTICIDE_CONTRACT = FactoryContract(FACTORY_INSECTICIDE_UP, FACTORY_INSECTICIDE_IN, FACTORY_INSECTICIDE_OUT, 3500)

FACTORY_PLASTIC_UP = FactoryUpgradeRequirement([
    ResourceRequirement(RES_ALUMINUM, 500),
    ResourceRequirement(RES_STEEL, 1000),
    ResourceRequirement(RES_CONCRETE, 16000),
    ResourceRequirement(RES_MONEY, 50000000),
])
FACTORY_PLASTIC_IN = [
    ResourceRequirement(RES_MONEY, 400),
    ResourceRequirement(RES_CRUDE_OIL, 1),
]
FACTORY_PLASTIC_OUT = ResourceRequirement(RES_PLASTIC, 10)
FACTORY_PLASTIC_CONTRACT = FactoryContract(FACTORY_PLASTIC_UP, FACTORY_PLASTIC_IN, FACTORY_PLASTIC_OUT, 1800)

FACTORY_LITHIUM_UP = FactoryUpgradeRequirement([
    ResourceRequirement(RES_GLASS, 1000),
    ResourceRequirement(RES_STEEL, 10000),
    ResourceRequirement(RES_CONCRETE, 25000),
    ResourceRequirement(RES_MONEY, 60000000),
])
FACTORY_LITHIUM_IN = [
    ResourceRequirement(RES_MONEY, 5000),
    ResourceRequirement(RES_LITHIUM_ORE, 115)
]
FACTORY_LITHIUM_OUT = ResourceRequirement(RES_LITHIUM, 5)
FACTORY_LITHIUM_CONTRACT = FactoryContract(FACTORY_LITHIUM_UP, FACTORY_LITHIUM_IN, FACTORY_LITHIUM_OUT, 750)

FACTORY_ACCUMULATOR_UP = FactoryUpgradeRequirement([
    ResourceRequirement(RES_ALUMINUM, 10000),
    ResourceRequirement(RES_GLASS, 6000),
    ResourceRequirement(RES_CONCRETE, 20000),
    ResourceRequirement(RES_MONEY, 100000000),
])
FACTORY_ACCUMULATOR_IN = [
    ResourceRequirement(RES_MONEY, 75000),
    ResourceRequirement(RES_LITHIUM, 20),
    ResourceRequirement(RES_ALUMINUM, 10),
    ResourceRequirement(RES_PLASTIC, 40),
]
FACTORY_ACCUMULATOR_OUT = ResourceRequirement(RES_ACCUMULATOR, 10)
FACTORY_ACCUMULATOR_CONTRACT = FactoryContract(FACTORY_ACCUMULATOR_UP, FACTORY_ACCUMULATOR_IN, FACTORY_ACCUMULATOR_OUT, 600)

FACTORY_WEAPONS_UP = FactoryUpgradeRequirement([
    ResourceRequirement(RES_BRICKS, 500000),
    ResourceRequirement(RES_GLASS, 10000),
    ResourceRequirement(RES_CONCRETE, 50000),
    ResourceRequirement(RES_MONEY, 200000000),
])
FACTORY_WEAPONS_IN = [
    ResourceRequirement(RES_MONEY, 250000),
    ResourceRequirement(RES_ACCUMULATOR, 1),
    ResourceRequirement(RES_STEEL, 1),
    ResourceRequirement(RES_ALUMINUM, 1),
]
FACTORY_WEAPONS_OUT = ResourceRequirement(RES_WEAPONS, 25)
FACTORY_WEAPONS_CONTRACT = FactoryContract(FACTORY_WEAPONS_UP, FACTORY_WEAPONS_IN, FACTORY_WEAPONS_OUT, 125)

FACTORY_SILICON_UP = FactoryUpgradeRequirement([
    ResourceRequirement(RES_GLASS, 1500),
    ResourceRequirement(RES_STEEL, 1200),
    ResourceRequirement(RES_CONCRETE, 20000),
    ResourceRequirement(RES_MONEY, 220000000),
])
FACTORY_SILICON_IN = [
    ResourceRequirement(RES_MONEY, 49500),
    ResourceRequirement(RES_SAND, 20),
    ResourceRequirement(RES_FUEL, 5),
    ResourceRequirement(RES_CLAY, 1),
]
FACTORY_SILICON_OUT = ResourceRequirement(RES_SILICON, 2)
FACTORY_SILICON_CONTRACT = FactoryContract(FACTORY_SILICON_UP, FACTORY_SILICON_IN, FACTORY_SILICON_OUT, 120)

FACTORY_CIRCUITRY_UP = FactoryUpgradeRequirement([
    ResourceRequirement(RES_ALUMINUM, 1000),
    ResourceRequirement(RES_GLASS, 8000),
    ResourceRequirement(RES_CONCRETE, 20000),
    ResourceRequirement(RES_MONEY, 300000000),
])
FACTORY_CIRCUITRY_IN = [
    ResourceRequirement(RES_MONEY, 5000),
    ResourceRequirement(RES_PLASTIC, 4),
    ResourceRequirement(RES_COPPER, 3),
    ResourceRequirement(RES_SILICON, 1),
]
FACTORY_CIRCUITRY_OUT = ResourceRequirement(RES_CIRCUITRY, 8)
FACTORY_CIRCUITRY_CONTRACT = FactoryContract(FACTORY_CIRCUITRY_UP, FACTORY_CIRCUITRY_IN, FACTORY_CIRCUITRY_OUT, 480)

FACTORY_TITANIUM_UP = FactoryUpgradeRequirement([
    ResourceRequirement(RES_GLASS, 2500),
    ResourceRequirement(RES_STEEL, 10000),
    ResourceRequirement(RES_CONCRETE, 30000),
    ResourceRequirement(RES_MONEY, 350000000),
])
FACTORY_TITANIUM_IN = [
    ResourceRequirement(RES_MONEY, 10000),
    ResourceRequirement(RES_ILMENITE, 8)
]
FACTORY_TITANIUM_OUT = ResourceRequirement(RES_TITANIUM, 4)
FACTORY_TITANIUM_CONTRACT = FactoryContract(FACTORY_TITANIUM_UP, FACTORY_TITANIUM_IN, FACTORY_TITANIUM_OUT, 320)

FACTORY_SILVER_UP = FactoryUpgradeRequirement([
    ResourceRequirement(RES_GLASS, 1500),
    ResourceRequirement(RES_STEEL, 15000),
    ResourceRequirement(RES_CONCRETE, 35000),
    ResourceRequirement(RES_MONEY, 750000000),
])
FACTORY_SILVER_IN = [
    ResourceRequirement(RES_MONEY, 10000),
    ResourceRequirement(RES_SILVER_ORE, 8)
]
FACTORY_SILVER_OUT = ResourceRequirement(RES_SILVER, 50)
FACTORY_SILVER_CONTRACT = FactoryContract(FACTORY_SILVER_UP, FACTORY_SILVER_IN, FACTORY_SILVER_OUT, 3000)

FACTORY_GOLD_UP = FactoryUpgradeRequirement([
    ResourceRequirement(RES_GLASS, 20000),
    ResourceRequirement(RES_STEEL, 20000),
    ResourceRequirement(RES_CONCRETE, 20000),
    ResourceRequirement(RES_MONEY, 1000000000),
])
FACTORY_GOLD_IN = [
    ResourceRequirement(RES_MONEY, 20000),
    ResourceRequirement(RES_GOLD_ORE, 20),
]
FACTORY_GOLD_OUT = ResourceRequirement(RES_GOLD, 3)
FACTORY_GOLD_CONTRACT = FactoryContract(FACTORY_GOLD_UP, FACTORY_GOLD_IN, FACTORY_GOLD_OUT, 240)

FACTORY_FERTILIZER_UP = FactoryUpgradeRequirement([
    ResourceRequirement(RES_BRICKS, 2500),
    ResourceRequirement(RES_LIMESTONE, 500),
    ResourceRequirement(RES_CONCRETE, 5000),
    ResourceRequirement(RES_MONEY, 4000000),
])
FACTORY_FERTILIZER_IN = [
    ResourceRequirement(RES_MONEY, 90),
    ResourceRequirement(RES_LIMESTONE, 8)
]
FACTORY_FERTILIZER_OUT = ResourceRequirement(RES_FERTILIZER, 11)
FACTORY_FERTILIZER_CONTRACT = FactoryContract(FACTORY_FERTILIZER_UP, FACTORY_FERTILIZER_IN, FACTORY_FERTILIZER_OUT, 1210)

FACTORY_TRUCKS_UP = FactoryUpgradeRequirement([
    ResourceRequirement(RES_BRICKS, 500000),
    ResourceRequirement(RES_CIRCUITRY, 90000),
    ResourceRequirement(RES_SILVER, 50000),
    ResourceRequirement(RES_MONEY, 2000000000),
])
FACTORY_TRUCKS_IN = [
    ResourceRequirement(RES_MONEY, 2500000),
    ResourceRequirement(RES_STEEL, 100),
    ResourceRequirement(RES_ACCUMULATOR, 25),
    ResourceRequirement(RES_SILVER, 50)
]
FACTORY_TRUCKS_OUT = ResourceRequirement(RES_TRUCKS, 50)
FACTORY_TRUCKS_CONTRACT = FactoryContract(FACTORY_TRUCKS_UP, FACTORY_TRUCKS_IN, FACTORY_TRUCKS_OUT, 100)

FACTORY_DRONE_UP = FactoryUpgradeRequirement([
    ResourceRequirement(RES_GLASS, 40000),
    ResourceRequirement(RES_PLASTIC, 120000),
    ResourceRequirement(RES_CONCRETE, 80000),
    ResourceRequirement(RES_MONEY, 2000000000),
])
FACTORY_DRONE_IN = [
    ResourceRequirement(RES_MONEY, 25000000),
    ResourceRequirement(RES_TITANIUM, 50),
    ResourceRequirement(RES_CIRCUITRY, 25),
    ResourceRequirement(RES_ACCUMULATOR, 250),
]
FACTORY_DRONE_OUT = ResourceRequirement(RES_DRONE, 1)
FACTORY_DRONE_CONTRACT = FactoryContract(FACTORY_DRONE_UP, FACTORY_DRONE_IN, FACTORY_DRONE_OUT, 1)

FACTORY_JEWELLERY_UP = FactoryUpgradeRequirement([
    ResourceRequirement(RES_BRICKS, 90000),
    ResourceRequirement(RES_GLASS, 20000),
    ResourceRequirement(RES_CONCRETE, 20000),
    ResourceRequirement(RES_MONEY, 500000000),
])
FACTORY_JEWELLERY_IN = [
    ResourceRequirement(RES_MONEY, 50000),
    ResourceRequirement(RES_DIAMOND, 1000),
    ResourceRequirement(RES_SILVER, 1),
    ResourceRequirement(RES_GOLD, 1),
]
FACTORY_JEWELLERY_OUT = ResourceRequirement(RES_JEWELLERY, 2)
FACTORY_JEWELLERY_CONTRACT = FactoryContract(FACTORY_JEWELLERY_UP, FACTORY_JEWELLERY_IN, FACTORY_JEWELLERY_OUT, 100)

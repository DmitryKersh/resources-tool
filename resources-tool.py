from pathlib import Path
import json

from classes import Factory, topNforUpgrade, bestConfig
from factories import FACTORY_CONTRACTS
from res import RESOURCES

CONFIG_PATH = Path('config.json')

FACTORY_ORDER = [
    'brick',
    'concrete',
    'fertilizer',
    'steel',
    'fuel',
    'glass',
    'copper',
    'insecticide',
    'aluminum',
    'plastic',
    'lithium',
    'accumulator',
    'weapons',
    'silicon',
    'circuitry',
    'titanium',
    'medtech',
    'silver',
    'gold',
    'jewellery',
    'drone',
    'trucks',
]

FACTORIES = [
    Factory(name, FACTORY_CONTRACTS[name], 0)
    for name in FACTORY_ORDER
]

HINT = '''
1 = Топ N апов заводов с твоего лвл
2 = Лучшее соотношение с нуля за N апов
'''


def build_default_config() -> dict:
    return {
        'factories': {
            factory.name: {
                'lvl': factory.lvl,
                'speed_mult': factory.speed_mult,
            }
            for factory in FACTORIES
        },
        'resources': {
            resource.name: resource.price
            for resource in RESOURCES
        },
    }


def save_config(config: dict) -> None:
    CONFIG_PATH.write_text(
        json.dumps(config, indent=4, ensure_ascii=False),
        encoding='utf-8',
    )


def load_config() -> dict:
    try:
        return json.loads(CONFIG_PATH.read_text(encoding='utf-8'))
    except FileNotFoundError:
        config = build_default_config()
        save_config(config)
        print('Не найден конфиг, поэтому он был создан заново. Перезапусти программу.')
        raise SystemExit
    except json.JSONDecodeError:
        config = build_default_config()
        save_config(config)
        print('Конфиг повреждён, поэтому он был пересоздан. Перезапусти программу.')
        raise SystemExit


def apply_config(config: dict) -> None:
    factory_config = config.get('factories', {})
    for factory in FACTORIES:
        data = factory_config.get(factory.name)
        if not data:
            continue

        factory.lvl = int(data.get('lvl', factory.lvl))
        factory.speed_mult = float(data.get('speed_mult', factory.speed_mult))

    resource_config = config.get('resources', {})
    for resource in RESOURCES:
        if resource.name in resource_config:
            resource.price = float(resource_config[resource.name])


def run() -> None:
    config = load_config()
    apply_config(config)

    match input(HINT).strip():
        case '1':
            n = int(input('Топ сколько показать? '))
            for line in topNforUpgrade(FACTORIES, n):
                print(line)

        case '2':
            upgrade_count = int(input('Сколько апов? '))
            for line in bestConfig(FACTORIES, upgrade_count):
                print(line)

        case _:
            print('Неизв. команда')

    input()


if __name__ == '__main__':
    run()
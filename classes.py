from __future__ import annotations

from dataclasses import dataclass
from heapq import heapify, heappop, heappush
from math import inf
from typing import Iterable


@dataclass(slots=True)
class Resource:
    name: str
    price: float


@dataclass(frozen=True, slots=True)
class ResourceRequirement:
    res: Resource
    amount: int

    def value(self) -> float:
        return self.amount * self.res.price


@dataclass(frozen=True, slots=True)
class FactoryUpgradeRequirement:
    reslist: tuple[ResourceRequirement, ...]

    def __init__(self, reslist: Iterable[ResourceRequirement]):
        object.__setattr__(self, 'reslist', tuple(reslist))

    def value(self) -> float:
        return sum(req.value() for req in self.reslist)


@dataclass(frozen=True, slots=True)
class FactoryContract:
    upgrade_req: FactoryUpgradeRequirement
    req: tuple[ResourceRequirement, ...]
    output: ResourceRequirement
    hourspeed: int

    def __init__(
        self,
        upgrade_req: FactoryUpgradeRequirement,
        req: Iterable[ResourceRequirement],
        output: ResourceRequirement,
        hourspeed: int,
    ):
        object.__setattr__(self, 'upgrade_req', upgrade_req)
        object.__setattr__(self, 'req', tuple(req))
        object.__setattr__(self, 'output', output)
        object.__setattr__(self, 'hourspeed', hourspeed)


@dataclass(slots=True)
class Factory:
    name: str
    contract: FactoryContract
    lvl: int
    speed_mult: float = 1.0


def calc_hour_profit_1lvl(contract: FactoryContract) -> float:
    in_val = sum(resreq.value() for resreq in contract.req)
    out_val = contract.output.value()
    return (out_val - in_val) / contract.output.amount * contract.hourspeed


def calc_upgrade_cost(upgrade_req: FactoryUpgradeRequirement, target_lvl: int) -> float:
    return target_lvl ** 2 * upgrade_req.value()


def calc_upgrade_okup_time(fac: Factory) -> float:
    profit = calc_hour_profit_1lvl(fac.contract) * fac.speed_mult
    if profit <= 0:
        return inf
    return calc_upgrade_cost(fac.contract.upgrade_req, fac.lvl + 1) / profit


def str_speed_mult(fac: Factory) -> str:
    return f"(speed x{fac.speed_mult})" if fac.speed_mult != 1 else ""


def topNforUpgrade(curr_list: list[Factory], n: int) -> list[str]:
    ret: list[str] = []
    heap = [(calc_upgrade_okup_time(fac), idx) for idx, fac in enumerate(curr_list)]
    heapify(heap)

    for _ in range(n):
        okup, idx = heappop(heap)
        fac = curr_list[idx]

        ret.append(
            f"{fac.name:<12} {fac.lvl + 1:<4}: {round(okup, 1)} hours {str_speed_mult(fac)}"
        )

        fac.lvl += 1
        heappush(heap, (calc_upgrade_okup_time(fac), idx))

    return ret


def bestConfig(curr_list: list[Factory], upgrade_count: int) -> list[str]:
    for fac in curr_list:
        fac.lvl = 0

    heap = [(calc_upgrade_okup_time(fac), idx) for idx, fac in enumerate(curr_list)]
    heapify(heap)

    for _ in range(upgrade_count):
        _, idx = heappop(heap)
        fac = curr_list[idx]
        fac.lvl += 1
        heappush(heap, (calc_upgrade_okup_time(fac), idx))

    return [f"{fac.name:<12}: {fac.lvl} {str_speed_mult(fac)}" for fac in curr_list]
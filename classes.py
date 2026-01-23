class Resource:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class ResourceRequirement:
    def __init__(self, res: Resource, amount: int):
        self.res = res
        self.amount = amount

    def value(self):
        return self.amount * self.res.price

class FactoryUpgradeRequirement:
    def __init__(self, reslist: list[ResourceRequirement]):
        self.reslist = reslist

class FactoryContract:
    def __init__(self, upgrade_req: FactoryUpgradeRequirement, req: list[ResourceRequirement], output: ResourceRequirement, hourspeed: int):
        self.req = req
        self.output = output
        self.hourspeed = hourspeed
        self.upgrade_req = upgrade_req

class Factory:
    def __init__(self, name, contract:FactoryContract, lvl: int, speed_mult:float=1.0):
        self.name = name
        self.contract = contract
        self.lvl = lvl
        self.speed_mult = speed_mult

def topNforUpgrade(curr_list: list[Factory], N: int):
    ret = []
    okups = [calc_upgrade_okup_time(fac) for fac in curr_list]
    for x in range(N):
        idx = okups.index(min(okups))
        ret.append(f"{curr_list[idx].name:<12}{curr_list[idx].lvl + 1:<4}: {round(okups[idx], 1)} hours "  + str_speed_mult(curr_list[idx]))
        curr_list[idx].lvl += 1
        okups[idx] = calc_upgrade_okup_time(curr_list[idx])
    return ret

def bestConfig(curr_list: list[Factory], upgrade_count: int):
    for fac in curr_list:
        fac.lvl = 0
    okups = [calc_upgrade_okup_time(fac) for fac in curr_list]
    for x in range(upgrade_count):
        idx = okups.index(min(okups))
        curr_list[idx].lvl += 1
        okups[idx] = calc_upgrade_okup_time(curr_list[idx])
    return [f"{fac.name:<12}: {fac.lvl} " + str_speed_mult(fac) for fac in curr_list]

def calc_hour_profit_1lvl(contract: FactoryContract):
    in_val = sum([resreq.res.price * resreq.amount for resreq in contract.req])
    out_val = contract.output.amount * contract.output.res.price
    return (out_val - in_val) / contract.output.amount * contract.hourspeed

def calc_upgrade_cost(upgrade_req: FactoryUpgradeRequirement, target_lvl: int):
    return target_lvl**2 * sum([req.value() for req in upgrade_req.reslist])

def calc_upgrade_okup_time(fac: Factory):
    return calc_upgrade_cost(fac.contract.upgrade_req, fac.lvl + 1) / (calc_hour_profit_1lvl(fac.contract) * fac.speed_mult)

def str_speed_mult(fac: Factory):
    return f"(speed x{fac.speed_mult})" if fac.speed_mult != 1 else ""
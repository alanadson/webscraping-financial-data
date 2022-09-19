class RealEstateFund:
    def __init__(self, paper, segment, price, ffo_yield, dividend_yield, p_vp, market_value, liquidity, number_real,
                 pricer_per_m2, rent_per_m2, cap_rate, average_vacancy):
        self.paper = paper
        self.segment = segment
        self.price = price
        self.ffo_yield = ffo_yield
        self.dividend_yield = dividend_yield
        self.p_vp = p_vp
        self.market_value = market_value
        self.liquidity = liquidity
        self.number_real = number_real
        self.pricer_per_m2 = pricer_per_m2
        self.rent_per_m2 = rent_per_m2
        self.cap_rate = cap_rate
        self.average_vacancy = average_vacancy


class Strategy:
    def __init__(self, segment="", price_min=0, ffo_yield_min=0, dividend_yield_min=0, p_vp_min=0, market_value_min=0,
                 liquidity_min=0, number_real_min=0, pricer_per_m2_min=0, rent_per_m2_min=0, cap_rate_min=0,
                 average_vacancy_min=0):
        self.segment = segment
        self.price_min = price_min
        self.ffo_yield_min = ffo_yield_min
        self.dividend_yield_min = dividend_yield_min
        self.p_vp_min = p_vp_min
        self.market_value_min = market_value_min
        self.liquidity_min = liquidity_min
        self.number_real_min = number_real_min
        self.pricer_per_m2_min = pricer_per_m2_min
        self.rent_per_m2_min = rent_per_m2_min,
        self.cap_rate_min = cap_rate_min
        self.average_vacancy_min = average_vacancy_min

    def apply_strategy(self, fund: RealEstateFund):
        if self.segment != "":
            if fund.segment != self.segment:
                return False
        if fund.price < self.price_min \
                or fund.ffo_yield < self.ffo_yield_min \
                or fund.dividend_yield < self.dividend_yield_min \
                or fund.p_vp < self.p_vp_min \
                or fund.market_value < self.market_value_min \
                or fund.liquidity < self.liquidity_min \
                or fund.number_real < self.number_real_min \
                or fund.pricer_per_m2 < self.pricer_per_m2_min \
                or fund.cap_rate < self.cap_rate_min \
                or fund.average_vacancy < self.average_vacancy_min:
            return False
        return True

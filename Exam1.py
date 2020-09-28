def compound_interest(rate_per_period, periods, initial_amount):
    final_amount = (rate_per_period + 1)**periods * initial_amount
    return final_amount

def determine_compound_interest_rate(final_amount, initial_amount, periods):
    interest_rate = (final_amount/initial_amount)** -periods - 1
    return interest_rate


def linear_cost_approximation(fixed_cost, marginal_cost, units):
    variable_cost = marginal_cost * units
    manufacturing_cost =  variable_cost + fixed_cost
    return manufacturing_cost


def linear_marginal_cost(price1, quantity1, price2, quantity2):
    linear_marginal_cost = abs((price1 - price2)/(quantity1-quantity2))
    return linear_marginal_cost


def present_value(discount_rate, period, future_amount):
    value_now = (1+discount_rate)** -period * future_amount
    return value_now


def future_value(discount_rate, period, present_amount):
    value_later = (1 + discount_rate) ** period * present_amount
    return value_later


def net_present_value(discount_rate, period, revenue_list, cost_list):
    sum = revenue_list[0] - cost_list[0]
    for i in range(1, period+1):
        sum = sum + (1+discount_rate) ** -i * (abs(revenue_list[i]) - abs(cost_list[i]))
    NPV = round(sum, 2)
    return NPV


def annual_worth(discount_rate, period, NPV):

    AW = 1/100 * NPV
    while True:
        sum = 0
        for i in range(1, period+1):
            sum = sum + (1+discount_rate) ** -i * AW

        if sum < NPV:
            AW = AW + 1/10000 * NPV

        else:
            AW = AW - 1/10000 * NPV
            break

    return round(AW,4)


def internal_rate_return(period, revenue_list, cost_list):
    NPV = 1
    IRR = 0
    while NPV > 0.01:
        IRR = IRR + 0.0001
        NPV = net_present_value(IRR, period, revenue_list, cost_list)
    return IRR*100


def roof(discount_rate, period, fixed_cost):
    fixed_cost = abs(fixed_cost)
    AW = annual_worth(discount_rate, period, fixed_cost)
    return AW



if __name__ == "__main__":

    # linear cost estimate
    fixed_cost = 1000
    price1, quantity1 = 1000, 12
    price2, quantity2 = 2300, 25
    marginal_cost = linear_marginal_cost(price1, quantity1, price2, quantity2)
    units = 30
    cost_estimate = linear_cost_approximation(fixed_cost, marginal_cost, units)
    print(f"Cost Estimate: {cost_estimate}")


    # net present value example
    discount_rate = 0.17
    periods = 5
    revenue_list = [18000, 0, 0, 0, 0, 0]
    cost_list = [0, 3600, 3600, 3600, 3600, 3600]
    npv = net_present_value(discount_rate, periods, revenue_list, cost_list)
    print(f"Net Present Value: {npv}")


    # annual worth example
    discount_rate = 0.17
    periods = 6
    npv = 197
    AW = annual_worth(discount_rate, periods, npv)
    print(f"Annual Worth: {AW}")


    # internal rate of return example
    periods = 10
    revenue_list = [0, 24, 45, 90, 108, 130, 156, 187, 224, 269, 322]
    cost_list = [100, 30, 36, 42, 50, 60, 73, 87, 105, 125, 150]
    IRR = internal_rate_return(periods, revenue_list, cost_list)
    print(f"Internal Rate of Return: {round(IRR,4)}%")


    # roof problem
    discount_rate = 0.10
    periods = 10
    initial_cost = 3500
    roof_aw = roof(discount_rate, periods, initial_cost)
    print(f"Roof Annual Worth: {roof_aw}")
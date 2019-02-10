"""
create method
in:
    state
    gross income
out
    net income after deducting state tax
assume:
    federal tax is 10%
"""

def calculate_net_income(gross,state):
    state_tax = {'CA':10,'NY':9,'TX':0,'NJ':6}
    #federal tax 10%
    gross *= 0.9
    #state tax
    if state in state_tax:
        tax = (100 - state_tax[state]) / 100
        gross *= tax
        print('Net income is '+ str(gross))
        return gross
    else:
        print("State not found")
        return None

x = calculate_net_income(100000,'CA')
print(x)
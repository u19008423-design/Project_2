print(
"The EPQ model determines the optimal quantity of an item to produce at a time.\n"
"It considers the demand for the item, the production rate, and the costs of setting up production and holding inventory.\n"
"The model helps determine how much should be produced in each production run while balancing these costs.\n"
"This helps a business avoid producing too much or too little inventory and manage production more efficiently.\n"
)

# 4. Worked Example
import math
# define inputs
annual_demand = 12000  # units per year
setup_cost = 50  # cost per production run, in Rand
holding_cost = 2  # cost per unit per year, in Rand
daily_demand_rate = 40  # units produced/sold per day
daily_production_rate = 100  # units your process can produce per day

# EPQ function
def calculate_epq(demand, setup, hold_cost, d_rate, p_rate):
    return math.sqrt((2 * demand * setup) / (hold_cost * (1 - d_rate / p_rate)))
epq = calculate_epq(annual_demand, setup_cost, holding_cost, daily_demand_rate, daily_production_rate)

# production runs per year and run length
runs_per_year = annual_demand / epq
run_length_days = epq / daily_production_rate

#maximum inventory level
max_inventory = epq * (1 - daily_demand_rate / daily_production_rate)

print("Optimal production quantity:", round(epq, 2))
print("Production runs per year:", round(runs_per_year, 2))
print("Length of each run(days):", round(run_length_days, 1))
print("Maximum inventory level:", round(max_inventory, 2))
print()
print()
print()





# 5 Try It Yourself

# answer 1
# change daily production rate- make it faster

annual_demand = 12000  # units per year
setup_cost = 50  # cost per production run, in Rand
holding_cost = 2  # cost per unit per year, in Rand
daily_demand_rate = 40  # units produced/sold per day
daily_production_rate = 150 # units your process can produce per day

# EPQ function
def calculate_epq(demand, setup, hold_cost, d_rate, p_rate):
    return math.sqrt((2 * demand * setup) / (hold_cost * (1 - d_rate / p_rate)))
epq = calculate_epq(annual_demand, setup_cost, holding_cost, daily_demand_rate, daily_production_rate)

# production runs per year and run length
runs_per_year = annual_demand / epq
run_length_days = epq / daily_production_rate

#maximum inventory level
max_inventory = epq * (1 - daily_demand_rate / daily_production_rate)

print("Optimal production quantity:", round(epq, 2))
print("Production runs per year:", round(runs_per_year, 2))
print("Length of each run(days):", round(run_length_days, 1))
print("Maximum inventory level:", round(max_inventory, 2))
print()
print(
"The EPQ goes down from 1000 to 905 units because a faster production rate (p) \n"
"fills daily demand much quicker, causing inventory to accumulate much faster during a run\n"
"To avoid high holding costs from this rapid buildup, the model recommends smaller batch sizes.\n"
"Mathematically, increasing p reduces the ratio(d/p)\n"
"which increases the denominator term in the EPQ formula\n"
"resulting in a smaller optimal batch size (production quantity). \n"
)
print()
print()
# answer 2
# change daily production rate- make it faster
annual_demand = 12000  # units per year
setup_cost = 50  # cost per production run, in Rand
holding_cost = 2  # cost per unit per year, in Rand
daily_demand_rate = 40  # units produced/sold per day
daily_production_rate = 100000 # units your process can produce per day

# EPQ function
def calculate_epq(demand, setup, hold_cost, d_rate, p_rate):
    return math.sqrt((2 * demand * setup) / (hold_cost * (1 - d_rate / p_rate)))
epq = calculate_epq(annual_demand, setup_cost, holding_cost, daily_demand_rate, daily_production_rate)

# production runs per year and run length
runs_per_year = annual_demand / epq
run_length_days = epq / daily_production_rate

#maximum inventory level
max_inventory = epq * (1 - daily_demand_rate / daily_production_rate)

print("Optimal production quantity:", round(epq, 2))
print("Production runs per year:", round(runs_per_year, 2))
print("Length of each run(days):", round(run_length_days, 1))
print("Maximum inventory level:", round(max_inventory, 2))
print()
print(
"When daily production rate p is increased to 100000, the EPQ yields 774.75(775) units\n"
"which is virtually identical to the plain EOQ value of 774.60(775) units. \n"
"This occurs because producing at 100 000 units per day satisfies the batch requirement almost instantaneously\n"
"meaning negligible inventory is sold during production.\n"
"Mathematically, as p grows extremely large, the ratio (d / p) approaches 0,\n"
"making the denominator term (1 - d/p) effectively 1.\n"
"Consequently, the EPQ formula, converges directly into the plain EOQ formula\n"
"proving that EOQ is simply a special case of EPQ with infinite production speed.\n"
)
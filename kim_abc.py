# 
print(
"The ABC classification model groups inventory items (SKUs) based on how much value they contribute to the overall inventory.\n"
"The value of each SKU is measured using its usage value, which is calculated as the demand for the item multiplied by its cost per unit.\n"
"A items are the highest-value items, B items have a medium value, and C items have the lowest value.\n"
"This helps a business identify which inventory items require the most attention and monitoring.\n"
)

# 4 Worked Example
# Step 1: sku data
sku_worked = [ 
{"sku": "BRK-100", "demand": 2000,  "cost": 45}, 
{"sku": "GSK-220", "demand": 1500,  "cost": 30}, 
{"sku": "BLT-010", "demand": 10000, "cost": 2}, 
{"sku": "BRG-330", "demand": 800,   "cost": 60}, 
{"sku": "SEAL-500","demand": 3000,  "cost": 5}, 
{"sku": "MTR-700", "demand": 50,    "cost": 800}, 
{"sku": "WSH-050", "demand": 20000, "cost": 0.5}, 
{"sku": "CBL-900", "demand": 400,   "cost": 25}, 
]
# Step 2: Calculate usage value per SKU
def  usage_value(demand, cost):
    return demand * cost

for item in sku_worked:
    item["value"] = usage_value(item["demand"], item["cost"])

# Step 3: Sort descending by value
sku_worked_sorted = sorted(sku_worked, key=lambda item: item["value"], reverse=True)

# Step 4: Calculate cumulative percentage
total_value = sum(item["value"] for item in sku_worked_sorted)

running_total = 0
for item in sku_worked_sorted:
    running_total += item["value"]
    item["cum_pct"] = (running_total / total_value) * 100  

# Step 5: Assign a tier
def assign_tier(cum_pct):
    if cum_pct <= 80:
        return "A"
    elif cum_pct <= 95:
        return "B"
    else:
        return "C"

for item in sku_worked_sorted:
    item["tier"] = assign_tier(item["cum_pct"])

# Step 6: Classification report
for item in sku_worked_sorted:
    print(
        item["sku"],"| value:", int(item["value"]), 
          "| cum %:",round(item["cum_pct"], 1),
          "| tier:", 
          item["tier"])

# Step 7: Count SKUs per tier
tier_counts = {"A": 0, "B": 0, "C": 0}
for item in sku_worked_sorted:
    tier_counts[item["tier"]] += 1

print("Tier Counts:", tier_counts, "\n")








# 5 Try It Yourself

#answer 1
# add two more SKUs without threshold change
# Step 1: Calculate usage value per SKU
skus = [ 
{"sku": "BRK-100", "demand": 2000,  "cost": 45}, 
{"sku": "GSK-220", "demand": 1500,  "cost": 30}, 
{"sku": "BLT-010", "demand": 10000, "cost": 2}, 
{"sku": "BRG-330", "demand": 800,   "cost": 60}, 
{"sku": "SEAL-500","demand": 3000,  "cost": 5}, 
{"sku": "MTR-700", "demand": 50,    "cost": 800}, 
{"sku": "WSH-050", "demand": 20000, "cost": 0.5}, 
{"sku": "CBL-900", "demand": 400,   "cost": 25}, 
{"sku": "NUT-200", "demand": 5000,  "cost": 1}, 
{"sku": "PIN-300", "demand": 6000,  "cost": 1.5}

]
# Step 2: Calculate usage value per SKU
def  usage_value(demand, cost):
    return demand * cost


for item in skus:
    item["value"] = usage_value(item["demand"], item["cost"])

# Step 3: Sort descending by value
skus_sorted = sorted(skus, key=lambda item: item["value"], reverse=True)

# Step 4: Calculate cumulative percentage
total_value = sum(item["value"] for item in skus_sorted)

running_total = 0
for item in skus_sorted:
    running_total += item["value"]
    item["cum_pct"] = (running_total / total_value) * 100   

# Step 5: Assign a tier
def assign_tier(cum_pct):
    if cum_pct <= 80:
        return "A"
    elif cum_pct <= 95:
        return "B"
    else:
        return "C"

for item in skus_sorted:
    item["tier"] = assign_tier(item["cum_pct"])

# Step 6: Classification report
for item in skus_sorted:
    print(
        item["sku"],"| value:", int(item["value"]), 
          "| cum %:",round(item["cum_pct"], 1),
          "| tier:", 
          item["tier"])

# Step 7: Count SKUs per tier
tier_counts = {"A": 0, "B": 0, "C": 0}
for item in skus_sorted:
    tier_counts[item["tier"]] += 1

print("Tier Counts:", tier_counts)
answer1 = (
    "The tier distribution changes slightly. "
    "After adding the two new SKUs, there are 4 A-tier, "
    "3 B-tier, and 3 C-tier SKUs. "
)
print(answer1, "\n")





#answer 2
# following from answer1 with updated thresholds

# Step 2: Calculate usage value per SKU
def  usage_value(demand, cost):
    return demand * cost

for item in skus:
    item["value"] = usage_value(item["demand"], item["cost"])

# Step 3: Sort descending by value
skus_sorted = sorted(skus, key=lambda item: item["value"], reverse=True)

# Step 4: Calculate cumulative percentage
total_value = sum(item["value"] for item in skus_sorted)

running_total = 0
for item in skus_sorted:
    running_total += item["value"]
    item["cum_pct"] = (running_total / total_value) * 100   

# Step 5: Assign a tier
def assign_tier(cum_pct):
    if cum_pct <= 70:
        return "A"
    elif cum_pct <= 90:
        return "B"
    else:
        return "C"

for item in skus_sorted:
    item["tier"] = assign_tier(item["cum_pct"])

# Step 6: Classification report
for item in skus_sorted:
    print(
        item["sku"],"| value:", int(item["value"]), 
          "| cum %:",round(item["cum_pct"], 1),
          "| tier:", 
          item["tier"])

# Step 7: Count SKUs per tier
tier_counts = {"A": 0, "B": 0, "C": 0}
for item in skus_sorted:
    tier_counts[item["tier"]] += 1

print("Tier Counts:", tier_counts)
answer2 = (
"After changing the tier thesholds to 70 and 90. "
"the tier counts become A = 3, B =3 and C = 4. "
"This results in fewer SKUs in the A-tier and more in the C-tier."
)
print(answer2, "\n")





# answer 3
# combined function with data input follow up from answer 2
def classify_inventory(skus):
    # 1. Calculate annual value directly
    for item in skus:
        item["value"] = item["demand"] * item["cost"]

    skus_sorted = sorted(
        skus,
        key=lambda item: item["value"],
        reverse=True
    )
    total_value = sum(item["value"] for item in skus_sorted)
    running_total = 0
    for item in skus_sorted:
        running_total += item["value"]
        item["cum_pct"] = (running_total / total_value) * 100

    def assign_tier(cum_pct):
        if cum_pct <= 70:
            return "A"
        elif cum_pct <= 90:
            return "B"
        else:
            return "C"

    for item in skus_sorted:
        item["tier"] = assign_tier(item["cum_pct"])

    report_table = []
    for item in skus_sorted:
        line = "{} | value: {} | cum %: {} | tier: {}".format(
            item["sku"],
            int(item["value"]),
            round(item["cum_pct"], 1),
            item["tier"]
        )
        report_table.append(line)

    tier_counts = {"A": 0, "B": 0, "C": 0}
    for item in skus_sorted:
        tier_counts[item["tier"]] += 1

    return report_table, tier_counts

print("\nclassification report:\n", "\n".join(classify_inventory(skus)[0]), sep="")
print("\nTier Counts:", classify_inventory(skus)[1])
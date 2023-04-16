import pandas as pd
import numpy as np

# Define the size of the dataset
n_samples = 10000

# Define the range of values for each column
size_range = (500, 5000)
location_options = ['Urban', 'Rural', 'Suburban']
market_demand_range = (5000, 50000)
production_cost_range = (10000, 100000)
compliance_cost_range = (1000, 10000)
performance_options = ['Good', 'Bad', np.nan]
financing_options = ['High', 'Medium', 'Low']
raw_material_options = ['High', 'Medium', 'Low']

# Generate random values for each column
size = np.random.randint(size_range[0], size_range[1], n_samples)
location = np.random.choice(location_options, n_samples)
market_demand = np.random.randint(market_demand_range[0], market_demand_range[1], n_samples)
market_demand[np.random.choice(n_samples, n_samples // 10)] = np.nan # Set 10% of values to NaN
production_costs = np.random.randint(production_cost_range[0], production_cost_range[1], n_samples)
compliance_costs = np.random.randint(compliance_cost_range[0], compliance_cost_range[1], n_samples)
compliance_costs[np.random.choice(n_samples, n_samples // 10)] = np.nan # Set 10% of values to NaN
performance = np.random.choice(performance_options, n_samples)
financing_availability = np.random.choice(financing_options, n_samples)
raw_material_availability = np.random.choice(raw_material_options, n_samples)
raw_material_availability[np.random.choice(n_samples, n_samples // 10)] = np.nan # Set 10% of values to NaN
good_investment = np.random.randint(0, 2, n_samples)

# Create a dictionary of the data
data = {'Size (sq. meters)': size,
        'Location': location,
        'Market Demand': market_demand,
        'Production Costs': production_costs,
        'Compliance Costs': compliance_costs,
        'Historical Performance': performance,
        'Financing Availability': financing_availability,
        'Raw Material Availability': raw_material_availability,
        'Good Investment (Label)': good_investment}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Write the DataFrame to a CSV file
df.to_csv('chemical_plant_investment_large.csv', index=False)

import pandas as pd
import numpy as np

# Set randon seed for reproducibility
np.random.seed(42)

# Generate 500 events
n = 500
event_types = ['Wedding', 'Corporate', 'Networking']
seasons = ['Spring', 'Summer', 'Winter']

df = pd.DataFrame({
    'event_type': np.random.choice(event_types, n),
    'guest_count': np.random.randint(30, 400, n),
    'food_cost': np.random.randint(1000, 8000, n),
    'labor_hours': np.random.randint(20, 200, n),
    'beverage_cost': np.random.randint(200, 2000, n),
    'equipment_cost': np.random.randint(100, 1000, n),
    'season': np.random.choice(seasons, n),
})

# Create synthetic revenue based on a rough formula +  noise
df['revenue'] = (
    df['food_cost'] * 1.5 +
    df['labor_hours'] * 25 +
    df['beverage_cost'] * 1.2 +
    df['equipment_cost'] * 1.1 +
    np.random.normal(0, 1000, n)
)

# Save to CSV
df.to_csv('data/synthetic_catering_data.csv', index=False)
print("✅ Dataset saved to data/synthetic_catering_data.csv")
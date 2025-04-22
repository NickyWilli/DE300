import os
import pandas as pd

# Ensure the output folder exists
os.makedirs('output', exist_ok=True)

df = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30]
})

df.to_csv('output/ec2_output.csv', index=False)
print("CSV file created!")

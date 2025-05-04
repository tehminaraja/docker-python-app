import pandas as pd

data = {
    'Name': ['Ali', 'Sara', 'John'],
    'Age': [25, 30, 35]
}

df = pd.DataFrame(data)

print("Data inside Docker container:")
print(df)

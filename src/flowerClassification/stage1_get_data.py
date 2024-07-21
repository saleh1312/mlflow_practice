from sklearn.datasets import load_iris
import pandas as pd
import json

iris = load_iris()



df_iris = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df_iris['target'] = iris.target



metadata = {
    'description': 'this is raw data',
}


data_dict = df_iris.to_dict(orient='records')
combined = {
    'metadata': metadata,
    'data': data_dict
}


with open('assets/feature_store/raw_data.json', 'w') as f:
    json.dump(combined, f, indent=4)

print("Data with metadata saved to 'data_with_metadata.json'")
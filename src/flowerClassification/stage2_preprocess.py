
import pandas as pd
import json
from flowerClassification.utils import save_df_as_json
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


with open('assets/feature_store/raw_data.json', 'r') as f:
    combined = json.load(f)


metadata = combined['metadata']
print(metadata["description"])
data = combined['data']


df = pd.DataFrame(data)



df.head()


df["target"].value_counts()


# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df.drop(columns=["target"]))



from flowerClassification.config import config



# Apply PCA
pca = PCA(n_components=config.prep.pca_comps_count)
X_pca = pca.fit_transform(X_scaled)





prep_df = pd.DataFrame(X_pca,columns = [str(i) for i in range( X_pca.shape[1] )])





prep_df["target"] = df["target"]





prep_df.head()




save_df_as_json(prep_df , 'this is pca data from raw' , 'assets/feature_store/pca_data.json')



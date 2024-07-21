import json


def save_df_as_json(df , metadesc , path):
    metadata = {
        'description': metadesc,
    }
    data_dict = df.to_dict(orient='records')
    combined = {
        'metadata': metadata,
        'data': data_dict
    }

    with open(path, 'w') as f:
        json.dump(combined, f, indent=4)



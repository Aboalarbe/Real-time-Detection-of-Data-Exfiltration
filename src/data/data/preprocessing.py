import pandas as pd


def load_data(path):
    df = pd.read_csv(path)
    return df
    
def preprocessing(dataframe):
    data = dataframe.drop(['timestamp', 'longest_word', 'sld'], axis=1)
    return data
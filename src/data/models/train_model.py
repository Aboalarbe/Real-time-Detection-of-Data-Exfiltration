import numpy as np
from sklearn.model_selection import train_test_split
from catboost import CatBoostClassifier, Pool
import pickle
import sys

'''training CatBoost model because it has the best accuracy
    for model comparison please see  the notebook in notebooks/model comparison.ipynb'''
    
def train_model(data): 
    X = data.drop(columns=['Label']).values
    y = data['Label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, shuffle=True, random_state=0)
    
    train_dataset = Pool(X_train, y_train, feature_names=list(data.drop(columns=['Label']).columns))
    model_params = {'iterations': 1000,
    'loss_function': 'Logloss',
    'depth': 4,
    'learning_rate': 0.02,
    'train_dir': 'crossentropy',
    'allow_writing_files': False,
    'random_seed': 42}
    
    model = CatBoostClassifier(**model_params)
    model.fit(train_dataset, verbose=False, plot=False)
    return model
    

def save_model(model):
    sys.path.append('../')
    with open(r'models/model.pkl','wb') as model_pkl:
        pickle.dump(model, model_pkl, protocol=2)

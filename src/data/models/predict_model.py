import pickle

# load saved model
def load_model(path):
    model = pickle.load(open(path, 'rb'))
    return model

# predict label and confidence score
def predict(row, model):
    label = model.predict(row.values)
    confidence = round(model.predict_proba(row.values)[0][label[0]], 2)
    return label, confidence
    
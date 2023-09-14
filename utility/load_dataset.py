import pickle

def load_train_data(folder_name):
    with open(folder_name, 'rb') as f:
        train_data = pickle.load(f)
    X_train, y_train = train_data['features'], train_data['labels']
    return X_train, y_train

def load_validation_data(folder_name):
    with open(folder_name, 'rb') as f:
        val_data = pickle.load(f)
    X_val, y_val = val_data['features'], val_data['labels']
    return X_val, y_val

def load_test_data(folder_name):
    with open(folder_name, 'rb') as f:
        test_data = pickle.load(f)
    X_test, y_test = test_data['features'], test_data['labels']
    return X_test, y_test
    


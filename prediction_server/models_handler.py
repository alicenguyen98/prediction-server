import joblib
import pandas as pd
from . import config

models = dict()

def get_available_models():
    return [str(x) for x in models.keys()]

def predict(model_name, params):
    
    if model_name not in models:
        raise Exception("No such prediction model")
    
    model = models[model_name]

    # Remove excessive parameter
    params = {x: params[x] for x in params if x in model.X_names}

    if len(params) != len(model.X_names):
        raise Exception(f"Paramters missing: {[x for x in model.X_names if x not in params.keys()]}")

    df_params = pd.DataFrame(params, index=[0])[model.X_names]
    df_params = df_params.astype(model.X_dtypes)

    return model.predict(df_params)[0]
    
def init():
    conf = config.get()

    # load all models from path
    for model_name in conf['models']:
        try:
            model_path = conf['models'][model_name]
            model = joblib.load(model_path)
            models[model_name] = model
        except Exception as err:
            print(f'Failed to load model ({model_name}: {err}')

    print(f'Models loaded: {models.keys()}')
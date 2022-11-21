import pandas as pd
import settings

_cache = None

def data():

    global _cache

    if _cache is None:
        print(f"Dataframe cache is empty. Loading {settings.data_path}")
        data_file = settings.data_path
        df_adcs = pd.read_hdf(data_file,"adcs")
        df_tps=pd.read_hdf(data_file,"tps")
        t0=df_adcs.index.min()
        df_adcs.index=df_adcs.index-t0
        df_tps["time_start"]-=t0
        _cache = df_adcs,df_tps,t0
    else:
        print(f"Dataframe cache already loaded. Returning cached values")

    return _cache
import pandas as pd


# TODO break out interpolate/fill into a separate system eventually?
def df_dfuniformindex(df: pd.DataFrame,
                      resolution: str,
                      idx_lbl: str = None):
    """
    df must be indexed by time if timeseries data
    :param df: dataframe to be resampled
    :param resolution: new string resolution to resample at
    :param idx_lbl column label to use as index to resample if not already the index in the df
    :return:
    """

    if idx_lbl:
        df.set_index(idx_lbl, inplace=True)

    df = df[~df.index.duplicated(keep='first')]
    # wont work with duplicate indexes
    df_resampled = df.resample(resolution).interpolate(method='linear')
    df_resampled = df_resampled[~df_resampled.index.duplicated(keep='first')]
    df_resampled.dropna(inplace=True)

    if idx_lbl:
        df_resampled.reset_index(drop=False, inplace=True)

    return df_resampled


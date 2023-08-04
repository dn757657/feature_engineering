from typing import Union
from pandas import DataFrame, Series
from darts import TimeSeries

# use this to go back from darts timeseries: df = series.pd_dataframe()
# TODO move this shit to the modelling library under darts


def df_to_timeseries(
        X: DataFrame,
        y: Union[DataFrame, Series],
        value_col_name: str
):
    """
    convert a dataframe or series into a darts suitable input
    :param X:
    :param y:
    :param value_col_name:
    :return:
    """
    df = X.copy()
    df[value_col_name] = y
    series = TimeSeries.from_dataframe(df, time_col=df.index.name, value_cols=[value_col_name])
    return series


def split_to_darts_timeseries(
        x_train: DataFrame,
        x_test: DataFrame,
        y_train: Union[DataFrame, Series],
        y_test: Union[DataFrame, Series]
):
    """
    convert typical split dataset to darts suitable input
    :param x_train:
    :param x_test:
    :param y_train:
    :param y_test:
    :return:
    """

    darts_train = df_to_timeseries(x_train, y_train, 'target_column_name')
    darts_test = df_to_timeseries(x_test, y_test, 'target_column_name')

    return darts_train, darts_test

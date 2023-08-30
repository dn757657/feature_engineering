import pandas as pd
import talib

from pandas import DataFrame
from typing import List


def df_add_smas(
        df: DataFrame,
        calc_col: str,
        periods: List[int],
        naming_prefix: str = ''
) -> DataFrame:
    """
    ass some simple moving averages to a dataframe based on the target column
    :param df: must be sorted and indexed appropriately!
    :param calc_col:
    :param periods:
    :return:
    """

    for period in periods:
        df[f'{naming_prefix}_SMA_{period.__str__()}'] = talib.SMA(df[calc_col], timeperiod=period)

    return df


def df_add_emas(
        df: DataFrame,
        calc_col: str,
        periods: List[int],
        naming_prefix: str = ''
) -> DataFrame:
    """
    ass some simple moving averages to a dataframe based on the target column
    :param df: must be sorted and indexed appropriately!
    :param calc_col:
    :param periods: list of ema periods to add based on target col
    :return:
    """

    for period in periods:
        df[f'{naming_prefix}_EMA_{period.__str__()}'] = talib.EMA(df[calc_col], timeperiod=period)

    return df


def df_add_rsis(
        df: DataFrame,
        calc_col: str,
        periods: List[int],
        naming_prefix: str = ''
) -> DataFrame:
    """
    ass some simple moving averages to a dataframe based on the target column
    :param df: must be sorted and indexed appropriately!
    :param calc_col:
    :param periods:
    :return:
    """

    for period in periods:
        df[f'{naming_prefix}_RSI_{period.__str__()}'] = talib.RSI(df[calc_col], timeperiod=period)

    return df


def df_add_bbands(
        df: DataFrame,
        calc_col: str,
        periods: List[int],
        naming_prefix: str = ''
) -> DataFrame:
    """
    ass some simple moving averages to a dataframe based on the target column
    :param df: must be sorted and indexed appropriately!
    :param calc_col:
    :param periods:
    :return:
    """

    for period in periods:
        upper, middle, lower = talib.BBANDS(df[calc_col], timeperiod=period)
        df[f'{naming_prefix}_UpperBB_{period.__str__()}'] = upper
        df[f'{naming_prefix}_MiddleBB_{period.__str__()}'] = middle
        df[f'{naming_prefix}_LowerBB_{period.__str__()}'] = lower

    return df


# Calculate
# the VWAP (not directly available in TA-Lib, so we create a function for it)
def df_add_vwap(
        df,
        price_col: str,
        volume_col: str,
        naming_prefix: str = ''
) -> DataFrame:

    df['cumulative_volume'] = df[volume_col].cumsum()
    df['cumulative_pv'] = (df[price_col] * df[volume_col]).cumsum()
    df[f'{naming_prefix}_vwap'] = df['cumulative_pv'] / df['cumulative_volume']
    df.drop(columns=['cumulative_volume', 'cumulative_pv'], inplace=True)

    return df

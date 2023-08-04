def df_adddiffcolomn(df, column):
    """
    add a difference column, common/best practice in financial forecasting
    known as return modelling
    construct difference column such that the difference between the time based index
    and the next time based index is logged in the same row as the first time based index
    :param df:
    :param column:
    :return:
    """

    return
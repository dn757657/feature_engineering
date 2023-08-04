def df_add_forwarddiff_col(df, column_name):
    """
    add a difference column, common/best practice in financial forecasting
    known as return modelling
    construct difference column such that the difference between the time based index
    and the next time based index is logged in the same row as the first time based index
    :param df:
    :param column:
    :return:
    """
    # Shift the data up by one row
    shifted_column = df[column_name].shift(-1)

    # Subtract the shifted column from the original column
    difference = df[column_name] - shifted_column

    # Add the difference column to the DataFrame
    df[column_name + '_forwarddiff'] = difference

    return df
from pandas import DataFrame


def temporal_train_test_split(
        df: DataFrame,
        target_column: str,
        train_fraction: float = 0.8
):
    """
    split a temporal dataframe into train and test data
    :param df: data to split as pandas dataframe
    :param target_column: target feature column name
    :param train_fraction: fraction of data to use as training data
    :return:
    """
    # Calculate the index at which to split
    split_index = int(len(df) * train_fraction)

    # Split the data
    X_train = df.drop(target_column, axis=1).iloc[:split_index]
    y_train = df[target_column].iloc[:split_index]

    X_test = df.drop(target_column, axis=1).iloc[split_index:]
    y_test = df[target_column].iloc[split_index:]

    return X_train, X_test, y_train, y_test
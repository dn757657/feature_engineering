from featurewiz import FeatureWiz
from typing import Union
from pandas import DataFrame, Series


def df_featwizfeatures(x_train: Union[DataFrame, Series],
                       y_train: Union[DataFrame, Series],
                       x_test: Union[DataFrame, Series]
                       ):
    """
    for some reason putting anything in feature_end arg breaks this
    despite this being the indicated usage in the documentaiton
    :param x_train:
    :param y_train:
    :param x_test:
    :return:
    """
    fwiz = FeatureWiz(
        corr_limit=0.70,
        feature_engg='',
        category_encoders='',
        dask_xgboost_flag=False,
        nrows=None,
        verbose=0)

    X_train_selected = fwiz.fit_transform(x_train, y_train)
    X_test_selected = fwiz.transform(x_test)

    return X_train_selected, X_test_selected

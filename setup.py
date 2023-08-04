from setuptools import setup, find_packages

with open("./requirements.txt") as requirement_file:
    requirements = requirement_file.read().split()

setup(
    name="feature_engineering",
    description="feature engineering and cleaning",
    version="0.1.2",
    author="dn757657",
    author_email="dn757657@dal.ca",
    install_requires=requirements,
    packages=find_packages(include=['dn757657_data_pre_processing',
                                    'dn757657_feature_selection'],
                           exclude=['dn757657_ta_features']),  # package = any folder with an __init__.py file
)

#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['Team2324.csv'], 
    },
    install_requires=[
        'pandas', 
    ],
)


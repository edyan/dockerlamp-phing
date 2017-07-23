from setuptools import setup

setup(
    name='StakkrPhing',
    version='1.0',
    packages=['phing'],
    entry_points='''
        [stakkr.plugins]
        phing=phing.core:phing
    '''
)

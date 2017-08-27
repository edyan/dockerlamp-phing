from setuptools import setup

setup(
    name='StakkrPhing',
    version='3.5',
    packages=['phing'],
    entry_points='''
        [stakkr.plugins]
        phing=phing.core:phing
    '''
)

from setuptools import setup

setup(
    name='MarinaPhing',
    version='1.0',
    packages=['phing'],
    entry_points='''
        [marina.plugins]
        phing=phing.core:phing
    '''
)

from setuptools import setup

setup(
    name='ControlPanel',
    version='0.1',
    py_modules=['main'],
    install_requires=[
        'Flask',
        'paho-mqtt',
        'numpy',
        'json',
    ],
)
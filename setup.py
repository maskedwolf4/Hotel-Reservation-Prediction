from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements =  f.read().splitlines()

setup(
    name = "Hotel_Reservation_Prediction",
    author = "Meet_Wadekar",
    version = "1.0",
    packages = find_packages(),
    install_requires = requirements,
    )


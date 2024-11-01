from setuptools import find_packages, setup

setup(
    name="Exoplanet Archive API",
    version="0.1.0",
    description="A Python package for interacting with the NASA Exoplanet Archive API with local caching.",
    author="James Holmes",
    author_email="j.r.holmes@outlook.com",
    packages=find_packages(exclude=["scripts", "tests"]),
    install_requires=[],
    python_requires=">=3.6",
)

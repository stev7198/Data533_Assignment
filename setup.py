from setuptools import setup, find_packages

setup(
    name="hockeyStats",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.0.0",
    ],
    include_package_data=True,  # This ensures your CSV files are included in the package
    package_data={
        "hockeyStats.players.data": ["*.csv"],
        "hockeyStats.teamstats.data": ["*.csv"],
    },
    description="A Python package to analyze hockey player and team stats.",
)

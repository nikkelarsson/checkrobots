from setuptools import setup

setup(
        name="checkrobots",
        version="1.0",
        description="Simple tool to observe various sites' robots.txt files.",
        keywords="utility webscraping",
        author="Niklas",
        packages=["checkrobots"],
        install_requires=["requests"],
        entry_points={"console_scripts": ["checkrobots=checkrobots.main:main"]},
        include_package_data=True,
        zip_safe=False
        )

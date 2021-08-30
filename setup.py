from setuptools import setup

setup(
        name="checkrobots",
        version="1.0",
        description="Simple tool to view various site's robots.txt.",
        keywords="joke utility webscraping",
        author="Niklas",
        packages=["checkrobots"],
        install_requires=["requests"],
        entry_points={"console_scripts": ["checkrobots=checkrobots.main:main"]},
        include_package_data=True,
        zip_safe=False
        )

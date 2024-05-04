from setuptools import find_packages
from setuptools import setup

setup(
        name='flasktemp',
        version='1.0.0',
        description='Shows the weather on a local webpage using Flask micro web framework',
        author='tchatzian',
        author_email='harischatzi@tutanota.com',
        url='https://github.com/tchatzian/flasktemp',
        packages=['flasktemp'],
        include_package_data=True,
        zip_safe=False,
        scripts=['flasktemp/flasktemp.py']
)

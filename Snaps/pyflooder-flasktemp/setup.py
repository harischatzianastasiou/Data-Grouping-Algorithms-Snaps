from setuptools import find_packages
from setuptools import setup

setup(
        name='pyflooder-flasktemp',
        version='1.0.0',
        description='
                Runs an HTTP Flood Python script that could stop
                the webpage used in flasktemp',
        author='tchatzian',
        author_email='harischat@tutanota.com',
        url='https://github.com/tchatzian/pyflooder-flasktemp',
        packages=['pyflooder-flasktemp'],
        include_package_data=True,
        zip_safe=False,
        scripts=['pyflooder-flasktemp/pyflooder.py']
)

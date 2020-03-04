import os
from setuptools import setup

# with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
#     README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='otus2002web',
    version='0.1',
    packages=['otus'],
    include_package_data=True,
    license='GNU General Public License v3.0',
    description='famous people text',
    # long_description=README,
    url='https://github.com/DanteOnline/django-dantejcoder',
    author='Leo Orlov',
    author_email='iamdanteonline@gmail.com',
    keywords=['json', 'django', 'JsonResponse', 'encoder'],
    classifiers=[],
    entry_points={
        'console_scripts': [
            'famous = otus.main:main',
        ]
    },
)

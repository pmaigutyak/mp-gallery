
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='django-mp-gallery',
    version='1.0',
    description='Django gallery app',
    long_description=open('README.md').read(),
    author='Paul Maigutyak',
    author_email='pmaigutyak@gmail.com',
    url='https://github.com/pmaigutyak/mp-gallery',
    download_url='https://github.com/pmaigutyak/mp-gallery/archive/1.0.tar.gz',
    packages=['gallery'],
    license='MIT',
    install_requires=[
        'django-modeltranslation==0.11',
        'django-multiupload',
        'django-cleanup==0.4.2',
        'sorl-thumbnail==12.4a1',
        'awesome-slugify',
        'django-ordered-model',
        'django-pure-pagination',
    ]
)

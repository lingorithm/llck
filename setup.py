#! /usr/bin/python
from setuptools import setup
from io import open
# to install type:
# python setup.py install --root=/


def readme():
    with open('README.md', encoding="utf8") as f:
        return f.read()


setup(name='llck', version='0.1.0',
      author='Mohamed Mahrous',
      author_email='m.mahrous.94@gmail.com',
      url='https://github.com/lingorithm/llck',
      license='MIT',
      description="Lingorithm Language Core Kit",
      long_description=readme(),
      long_description_content_type='text/markdown',
      package_dir={'llck': 'llck', },
      packages=['llck'],
      classifiers=[
          'Development Status :: In Development',
          'Natural Language :: Arabic',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: Text Processing :: Linguistic :: NLP',
      ],
      )

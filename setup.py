from setuptools import setup

setup(name='Ward Python Package',
      version='0.1',
      description='Read matrix and run BLAST searches',
      url='TBD',
      author='Sarah Ward',
      author_email= 'sarah.ward-2@selu.edu',
      license='MIT',
      packages=['wardpythonpackage'],
      install_requires=[
          'dendropy',
          'biopython', 
          'pandas'],
      long_description=open('README.txt').read(),
zip_safe=True)
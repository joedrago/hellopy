from setuptools import setup

setup(name='hellopy',
      version='0.1',
      description='wat',
      url='http://github.com/joedrago/hellopy',
      author='Joe Drago',
      author_email='joedrago@gmail.com',
      license='BSD',
      entry_points={"console_scripts": ["hellopy = hellopy.main:main"]},
      packages=['hellopy'],
      zip_safe=False)

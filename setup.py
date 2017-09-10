# necessary to push to PyPI
# cf. http://peterdowns.com/posts/first-time-with-pypi.html
# cf. https://tom-christie.github.io/articles/pypi/


from setuptools import setup, find_packages

with open('README.rst') as f:
    long_description = f.read()

setup(
  name = 'ezvis3d',
  packages = ['ezvis3d'],
  version = '0.2',
  description = 'easy vis.js Graph3d js library wrapper, accessible from pandas dataframes in the IPython notebook',
  long_description = long_description,
  author = 'oscar6echo',
  author_email = 'olivier.borderies@gmail.com',
  url = 'https://github.com/oscar6echo/ezvis3d', # use the URL to the github repo
  download_url = 'https://github.com/oscar6echo/ezvis3d/tarball/v0.2', # tag number at the end
  keywords = ['vis.js', 'Graph3d', 'pandas', 'notebook', 'javascript'], # arbitrary keywords
  license='MIT',
  classifiers = [ 'Development Status :: 4 - Beta',
                  'License :: OSI Approved :: MIT License',
                  'Programming Language :: Python :: 2.7',
                  'Programming Language :: Python :: 3.5',
  ],
  include_package_data=True,
  package_data={
    'api':
         ['api/ezvis3d_dataset.json',
          'api/ezvis3d_dataset.tsv',
          'api/ezvis3d_method.json',
          'api/ezvis3d_method.tsv',
          'api/ezvis3d_option.json',
          'api/ezvis3d_option.tsv'
         ]
    },
)
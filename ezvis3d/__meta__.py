
__name__ = 'ezvis3d'
name_url = __name__.replace('_', '-')

__version__ = '0.2.5'
__description__ = 'easy vis.js Graph3d js library wrapper, accessible from pandas dataframes in the IPython notebook'
__long_description__ = 'See github repo'
__author__ = 'oscar6echo'
__author_email__ = 'olivier.borderies@gmail.com'
__url__ = 'https://github.com/{}/{}'.format(__author__,
                                            name_url)
__download_url__ = 'https://github.com/{}/{}/tarball/{}'.format(__author__,
                                                                name_url,
                                                                __version__)
__keywords__ = ['vis.js', 'Graph3d', 'pandas', 'notebook', 'javascript']
__license__ = 'MIT'
__classifiers__ = ['Development Status :: 4 - Beta',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6'
                   ]
__include_package_data__ = True
__package_data__ = {
    'api':
    ['api/ezvis3d_dataset.json',
     'api/ezvis3d_dataset.tsv',
     'api/ezvis3d_method.json',
     'api/ezvis3d_method.tsv',
     'api/ezvis3d_option.json',
     'api/ezvis3d_option.tsv'
     ]
}
__zip_safe__ = False
__entry_points__ = {}

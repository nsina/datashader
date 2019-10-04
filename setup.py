import os,sys
import shutil
from setuptools import find_packages, setup

# build dependencies
import param
import pyct.build

########## dependencies ##########

install_requires = [
    # `conda install dask[complete]` happily gives you dask...which is
    # happily like pip's dask[complete]. (conda's dask-core is more
    # like pip's dask.)
    'dask[complete] >=0.18.0',
    'toolz >=0.7.4',  # ? for some dask issue (dasks does only >=0.7.3)
    'datashape >=0.5.1',
    'numba >=0.37.0',
    'numpy >=1.7',
    'pandas >=0.20.3',
    'pillow >=3.1.1',
    'xarray >=0.9.6',
    'colorcet >=0.9.0',
    'param >=1.6.0',
    'pyct[cmd]',
    'scikit-image',
    'bokeh',
    'scipy',
]

extras_require = {
    'tests': [
        'pytest >=3.9.3',
        'pytest-benchmark >=3.0.0',
        'flake8',
        'nbsmoke >=0.2.6',
        'fastparquet >=0.1.6',  # optional dependency
        'pandas >=0.24.1',  # optional ragged array support
    ],
    'examples': [],
    'examples_extra':[
        'attrs',
        'beautifulsoup4',
        'bokeh',
        #'cachey', # TODO: investigate (no conda package
        'colorcet',
        'dill',
        'distributed', # dask
        'fastparquet >=0.2.1',
        'holoviews >=1.10.0',
        'hvplot >=0.4.0',
        'intake >=0.4.1',
        'intake-parquet',
        'jupyter',
        'jupyter_dashboards',
        'matplotlib',
        'networkx >=2.0',
        'pandas >=0.24.1',
        'panel >=0.4.0',
        'paramnb',
        'requests',
        'tblib',
        'xarray',
        'pyyaml <5.1',
        'streamz >=0.2.0',
        'webargs',
        ### conda only below here
        'cartopy',
        'graphviz',
        'python-graphviz',
        'fastparquet',
        'geoviews',
        'iris',
        'krb5',
        'pyproj',
        'pytables',
        'python-snappy',
        'rasterio',
        'snappy',
        'shapely',
        'statsmodels'
    ]
}

extras_require['doc'] = extras_require['examples_extra'] + [
    'nbsite >=0.5.2',
    'sphinx_ioam_theme',
    'numpydoc'
]

extras_require['all'] = sorted(set(sum(extras_require.values(), [])))



########## metadata for setuptools ##########

setup_args = dict(
    name='datashader',
    version=param.version.get_setup_version(__file__,"datashader",archive_commit="$Format:%h$"),
    description='Data visualization toolchain based on aggregating into a grid',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url='http://datashader.org',
    maintainer='Datashader developers',
    maintainer_email='dev@datashader.org',
    python_requires=">=2.7",
    install_requires=install_requires,
    extras_require=extras_require,
    tests_require=extras_require['tests'],
    license='New BSD',
    packages=find_packages(),
    include_package_data = True,
    entry_points={
        'console_scripts': [
            'datashader = datashader.__main__:main'
        ]
    },
)

if __name__ == '__main__':
    example_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                'datashader','examples')
    if 'develop' not in sys.argv:
        pyct.build.examples(example_path, __file__, force=True)

    setup(**setup_args)

    if os.path.isdir(example_path):
        shutil.rmtree(example_path)

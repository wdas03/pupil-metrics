import setuptools

package_dir = "src/pupil_metrics"

setuptools.setup(
    name='pupil-metrics',
    version='0.1.0',    
    description='Pupil metrics calculations from time-series data.',
    url='https://github.com/wdas03/pupil_metrics',
    author='Will Das',
    author_email='williamhdas@gmail.com',
    license='BSD 2-clause',
    include_package_data=False, 
    #packages=setuptools.find_packages(package_dir),
    package_dir={"": package_dir},
    install_requires=['pandas',
                      'numpy',                     
                      ]
)
from setuptools import setup, find_packages

setup(
    name='demo2',
    version='0.3.1',
    description='News for Django',
    author='Elias',
    # namespace_packages=['home'],  # line 8
    packages=find_packages(),
    platforms='any',
    #zip_safe=False,
    include_package_data=True,
    # dependency_links=['git+ssh://git@git.home.com/app-admintools@v0.1#egg=admintools-0.1'],  # line 13
    # install_requires=['admintools==0.1'],  # line 14
    # classifiers=[
    #     'Development Status :: 5 - Production/Stable',
    #     'Environment :: Web Environment',
    #     'Intended Audience :: Developers',
    #     'License :: OSI Approved :: BSD License',
    #     'Operating System :: OS Independent',
    #     'Programming Language :: Python',
    #     'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    #     'Framework :: Django',
    # ],
)

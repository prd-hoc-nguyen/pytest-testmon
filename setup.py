from setuptools import setup

setup(
    name='testmon',
    description='Test Runner for Python',
    version='0.2.6',
    license='MIT',
    platforms=['linux', 'osx', 'win32'],
    packages=['testmon'],
    scripts=['testmon/tmon.py'],
    url='http://igg.me/at/testmon',
    author_email='tibor.arpas@infinit.sk',
    author='Tibor Arpas, Jozef Knaperek, Martin Riesz',
    data_files=([('', ['README.rst']), ]),
    entry_points={
        'pytest11': [
            'testmon = testmon.pytest_testmon',
        ]
    },
    install_requires=['pytest>=2.7.0,<2.8', 'pytest-cache>=1.0', 'watchdog>=0.8',
                      'coverage>=3.7.1,<4.0'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Programming Language :: Python', ],
)

import os
from setuptools import setup

# defang
# Defangs and refangs malicious URLs


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="defang",
    version="0.2.1",
    description="Defangs and refangs malicious URLs",
    author="Johan Nestaas",
    author_email="johannestaas@gmail.com",
    license="GPLv3+",
    keywords="",
    url="https://www.bitbucket.org/johannestaas/defang",
    packages=['defang'],
    package_dir={'defang': 'defang'},
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Environment :: Console',
        'Environment :: X11 Applications :: Qt',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
    ],
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'defang = defang.bin:defang',
        ],
    },
    test_suite="test"
)

from distutils.core import setup

setup(
    name='ostd',
    version='1.0.0',

    description='Downloads subtitles from OpenSubtitles',
    author='Philipp Ploder',
    url='https://github.com/Fylipp/ostd',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    keywords='opensubtitles',

    py_modules=['ostd'],
    requires=[
        'chardet'
    ]
)

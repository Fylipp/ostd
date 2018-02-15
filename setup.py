from distutils.core import setup

setup(
    name='ostd',
    version='1.0.0',
    description='Downloads subtitles from OpenSubtitles',
    author='Philipp Ploder',
    url='https://github.com/Fylipp/ostd',
    py_modules=['ostd'],
    install_requires=[
        'chardet'
    ]
)

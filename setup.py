import setuptools

setuptools.setup(
    name='rime',
    version='2.0.dev1',
    entry_points={"console_scripts": ["rime=rime._main:_main", "rime_init=rime.init._main:_main"]},
    packages=['rime', 'rime.init',
              'rime.basic', 'rime.basic.targets', 'rime.basic.util',
              'rime.core', 'rime.plugins', 'rime.plugins.judge_system',
              'rime.plugins.plus', 'rime.plugins.summary', 'rime.util'],
    package_dir={'rime': 'rime'},
    install_requires=['six', 'Jinja2'],
    tests_require=['pytest', 'mock'],
    package_data={'rime': ['plugins/summary/*.ninja']},
)

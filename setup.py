from setuptools import setup, find_packages

setup(
    name='kitty-ntfy-cmd',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    py_modules = [ 'kitty_ntfy_cmd' ],
    install_requires=['plyer', 'dbus-python'],
    data_files=[
        ('share/KittyNtfyCmd', ['share/kitty_ntfy_cmd_watcher.py'])
    ],
    entry_points='''
        [console_scripts]
        kitty-ntfy-cmd=KittyNtfyCmd.main:main
    ''',

    # metadata to display on PyPI
    author='Scott Hamilton',
    author_email='sgn.hamilton+python@protonmail.com',
    description='Python script and kitty watcher to make kitty post ntfy notifications when commands have finished executing',
    keywords='kitty ntfy',
    url='https://github.com/SCOTT-HAMILTON/kitty-ntfy-cmd',
    project_urls={
        'Source Code': 'https://github.com/SCOTT-HAMILTON/kitty-ntfy-cmd',
    },
    classifiers=[
        'License :: OSI Approved :: Python Software Foundation License'
    ]
)

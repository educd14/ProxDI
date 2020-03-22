from setuptools import setup, find_packages

setup(
    name="ProxDI",
    version="0.0.1",
    packages=find_packages(),
    author="Eduardo Collazo Dominguez",
    author_email="ecollazodominguez@danielcastelao.org",
    license="GLP",
    platforms="Unix",
    classifiers=["Development Status :: 3 - Alpha",
                "Environment :: Console",
                "Topic :: Software Development :: Libraries",
                "License :: OSI Aproved :: GNU General Public License",
                "Programming Language :: Python :: 3.4",
                "Operating System :: Linux Ubuntu"
                ],
    description="Proyecto DI",
    package_data={
        "": ["*.txt", "*.rst", "*.glade", "*.py"],
        "res": ["*"],
        "src": ["*"],
    },
    entry_points={
        "gui_scripts": [
            "ProxDI = src.Inicio:main_func"
        ]
    },
    install_requires=['PyGObject', 'pycairo']
)
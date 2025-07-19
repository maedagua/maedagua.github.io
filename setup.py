from setuptools import setup, find_packages

setup(
    name="divisor",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "click",
        "GitPython",
        "PyYAML",
    ],
    entry_points={
        "console_scripts": [
            "divisor = cli:main",
        ],
    },
)

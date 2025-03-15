from setuptools import setup, find_packages

def read_version():
    with open("encodex/version.py") as f:
        exec(f.read())
    return locals()["__version__"]

setup(
    name="encodex",
    version=read_version(),
    description="A Python package for string encoding, obfuscation, and encryption.",
    long_description="""Encodex is a Python package for string encoding, obfuscation, and encryption. It introduces a custom Base95 encoding method for string manipulation, designed for basic obfuscation and simple encryption tasks. 

### Features:
- Custom Base95 encoding for strings
- Obfuscation of Python code
- Cross-platform (Windows & macOS) support
- Detailed error logging and debugging

### Installation:
To install Encodex, simply run:
```bash
pip install encodex
````
""",
    long_description_content_type="text/markdown",
    author="loser",
    author_email="contact@losr.is-a.dev",
    url="https://github.com/madhead341/encodex",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Security :: Cryptography",
    ],
    install_requires=[
        "colorama",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "encodex = encodex.__main__:main",
        ]
    },
    include_package_data=True,
    zip_safe=False,
)

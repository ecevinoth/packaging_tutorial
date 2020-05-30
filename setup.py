import setuptools

with open("README.md", 'r') as fh:
    long_description = fh.read()


setuptools.setup(
    name="example-pkg-ecevinoth",
    version="0.0.2",
    author="vinoth",
    author_email="ecevinoth@gmail.com",
    description="a small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    package=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
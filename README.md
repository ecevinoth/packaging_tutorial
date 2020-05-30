# Example Package - Learning PyPi

This is a simple example package.

Following are the few input arguments to setuptools.setup() function.

1. *name*
2. *version*
3. *author*
4. *author_email*
5. *description*
6. *long_description*
7. *long_description_content_type*
8. *url*
9. *packages*
10. *classifiers*


## useful links
[list of useful classifiers.](https://pypi.org/classifiers/)
[help to choose license.](https://choosealicense.com/)
[For more markdown code.](https://guides.github.com/features/mastering-markdown/)



# procedure to create python package index
## pre-requisite
- upgrade setuptools : Library used to create package
    `python -m pip install --user --upgrade setuptools wheel`
- upgrade twine :  Library used to upload code into pypi server
    `python -m pip install --user --upgrade twine`
- account in [test pypi](https://test.pypi.org/account/register/)
- pypi api token [link](https://test.pypi.org/manage/account/#api-tokens)

## steps
generate distribution packages 
`python setup.py sdist bdist_wheel`

uploading the distributed package to test pypi server
`python -m twine upload --repository testpypi dist/*`

install
python3 -m pip install --index-url https://test.pypi.org/simple/ example-pkg-example-pkg-ecevinoth

## steps to upload in production PyPI
- Choose a memorable and unique name
- Register an account on https://pypi.org
- Use twine upload `python -m twine upload --repository testpypi dist/*`; the package will upload to https://pypi.org/ by default.

- Install your package from the real PyPI using pip install [your-package].

*EOF*
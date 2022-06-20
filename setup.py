import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='detr',
    version='0.2.1',
    author='Ivan Yovchev',
    author_email='ivan.yovchev@cboost.nl',
    description='Facebook DETR repo restructured into a python package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Ivan-Yovchev/detr',
    project_urls = {
        "Bug Tracker": "https://github.com/Ivan-Yovchev/detr/issues"
    },
    license='MIT',
    packages=['detr', 'detr.datasets', 'detr.d2', 'detr.d2.detr_d2', 'detr.models', 'detr.util'],
    # install_requires=['requests'],
)
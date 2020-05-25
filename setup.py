import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example_pkg_donaldstierman", # Replace with your own username
    version="0.0.10",
    author="Donald Stierman",
    author_email="stiermandon@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/donald/example_pkg_project",
    #packages=setuptools.find_packages(),
    packages=['example_pkg', 'tests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

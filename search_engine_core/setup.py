import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="search_engine_core",
    version="0.0.1",
    author="Amin",
    author_email="amin.mirakhorly@gmail.com",
    description="search_engine_core",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=[
        'db.models',
        *setuptools.find_packages()
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

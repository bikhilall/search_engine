import sys
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# The source dist comes with batteries included, the wheel can use pip to get the rest
is_wheel = 'bdist_wheel' in sys.argv

excluded = []
if is_wheel:
    excluded.append('extlibs.future')


def exclude_package(pkg):
    for exclude in excluded:
        if pkg.startswith(exclude):
            return True
    return False


def create_package_list(base_package):
    return (
            [base_package] + [
        base_package + '.' + pkg
        for pkg
        in setuptools.find_packages(base_package)
        if not exclude_package(pkg)
    ]
    )


setuptools.setup(
    name="search_engine_core",
    version="0.0.1",
    author="Amin",
    author_email="amin.mirakhorly@gmail.com",
    description="search_engine_core",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=create_package_list('search_engine_core'),
    install_requires=[
        'mysql-connector-python==8.0.19',
        'SQLAlchemy==1.3.13'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

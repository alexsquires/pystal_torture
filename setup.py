from setuptools import setup, find_packages
from pystal_torture import __version__ as VERSION

# readme = "README.md"
# with open(readme) as f:
#     long_description = f.read()

setup(
    description="pure python crystal torturing",
    author="Alex G. Squires",
    version=VERSION,
    install_requires=open("requirements.txt").read(),
    python_requires=">=3.8",
    license="MIT",
    packages=find_packages(exclude=["docs", "tests*"]),
    name="pystal-torture"
)

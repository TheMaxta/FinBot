from setuptools import setup, find_packages

setup(
    name="finance_app",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "PyMuPDF",
        "pydantic",
        # Add other dependencies here
    ],
    author="Maximillian Mahlke",
    author_email="max@softwareengineer.click",
    description="A personal finance app for parsing and analyzing bank statements",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/TheMaxta/FinBot",
)

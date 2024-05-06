from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="loggerpackage",
    version="1.0.0",
    description="Prove Of Concept",
    author="GUSTAVO LEAL SILVA E SOUZA",
    author_email="lses.gustavo@gmail.com",
    url="https://github.com/gusttaleal/poc-python-custom-logger-package",
    packages=find_packages(include=["loggerpackage", "loggerpackage.*"]),
    package_dir={"loggerpackage": "loggerpackage"},
    include_package_data=True,
    install_requires=[
        "opentelemetry-instrumentation-logging",
        "opentelemetry-semantic-conventions"
    ],
    python_requires=">=3"
)

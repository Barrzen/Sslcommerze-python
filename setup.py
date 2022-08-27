import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requires = [
    'requests==2.28.1'
]

setuptools.setup(
    name="sslcommerz-python",
    version="1.0.0",
    author="Piecoders IT Solutions",
    author_email="piecodersit@gmail.com",
    description="Implements SSLCOMMERZ payment gateway in python based web apps.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shahedex/sslcommerz-payment-gateway-python",
    packages=setuptools.find_packages(),
    install_requires=requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
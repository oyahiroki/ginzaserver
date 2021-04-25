import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ginzaserver",
    version="1.0.0.0",
    author="Hiroki Oya",
    author_email="oyahiroki@gmail.com",
    description="HTTP Server for GiNZA - Japanese NLP Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oyahiroki/ginzaserver",
    packages=setuptools.find_packages(),
    license='Apache License 2.0',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['ginzaserver = ginzaserver.ginzaserver:main']
    },
    python_requires='>=3.8',
)

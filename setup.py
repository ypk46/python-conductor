from setuptools import setup

setup(
    name="python-conductor",
    packages=["conductor"],
    version="0.2.0",
    description="A simple python wrapper for Netflix Conductor task execution",
    author="Yuyi Pacheco K.",
    author_email="yuyik46@gmail.com",
    url="https://github.com/ypk46/python-conductor",
    download_url="https://github.com/ypk46/python-conductor/archive/v0.1.0.tar.gz",
    keywords=["conductor"],
    license="MIT",
    install_requires=["requests"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)

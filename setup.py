from setuptools import setup

setup(
    name="foo",
    version="0.0.1",
    packages=['foo'],
    install_requires=["numba",
                      "sklearn",
                      "tqdm",
                      "anndata",
                      "skranger",
                      "fisher==0.1.9"
                     ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)

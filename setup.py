from setuptools import setup, find_packages


_REQUIRED = [
    "numpy",
    "einops",
    "tqdm",
    # TODO: remove this upper bound 
    # currently, when using ray we get:
    # "AttributeError: module 'pydantic._internal' has no attribute '_model_construction'"
    "click",
    "pydantic>=2.0.0,<2.5.0",
    "wandb",

    # for mamba stuff
    # "mamba_ssm", 
    # "causal_conv1d"
]

_OPTIONAL = {
    "analysis": [
        "pandas",
        "seaborn",
        "matplotlib",
    ],
    "extra":[
        "rich", 
        "ray",
        "PyYAML",
    ]
}

# ensure that torch is installed, and send to torch website if not
try:
    import torch
except ModuleNotFoundError:
    raise ValueError("Please install torch first: https://pytorch.org/get-started/locally/")

try:
    import transformers
except ModuleNotFoundError:
    raise ValueError("Please install transformers first: https://huggingface.co/transformers/installation.html")

setup(
    name="zoology",
    version="0.0.1",
    description="",
    author="simran sabri",
    packages=find_packages(),
    install_requires=_REQUIRED,
    extras_require=_OPTIONAL,
    include_package_data=True,
    entry_points={
        'console_scripts': ['zg=zoology.cli:cli'],
    },
)


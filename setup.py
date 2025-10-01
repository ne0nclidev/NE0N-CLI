```python
from setuptools import setup, find_packages

setup(
    name="neon-cli",
    version="0.9",
    description="Powerful CLI tool based in terminal.",
    author="???",
    packages=find_packages(),
    install_requires=[
        "colorama",
    ],
    entry_points={
        "console_scripts": [
            "neon-cli=neon_cli.cli:main",
        ],
    },
    python_requires=">=3.6",
)
```

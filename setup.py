from setuptools import setup, find_packages

setup(
    name="neon-cli",
    version="0.9",
    description="A pseudo-hacking terminal CLI with colored output and fun commands.",
    author="Your Name",
    packages=find_packages(),
    install_requires=["colorama"],
    entry_points={
        "console_scripts": [
            "neon-cli = neon_cli.cli:main"
        ]
    },
    python_requires=">=3.6",
)
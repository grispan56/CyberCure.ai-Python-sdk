import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cybercure",
    version="0.4.5",
    author="CyberCure.ai",
    author_email="contact@nucleon.sh",
    description="Python SDK to integrate cybercure.ai cyber intel feeds quickly and easily",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/grispan56/CyberCure.ai-Python-sdk",
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)

from setuptools import find_packages, setup

setup(
    name="prolllm",
    version="0.0.1",
    author="Louis Wendler",
    description="Prompt-LLM (prollm) - A fresh way to prompt your LLMs 🌟🚀",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords="",
    license="MIT License",
    url="https://github.com/1ucky40nc3/prollm",
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
)

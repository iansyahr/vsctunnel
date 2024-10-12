from setuptools import setup, find_packages

setup(
    name="vstunnel",
    version="0.1",
    packages=find_packages(),
    description="Developing a Google Colab project using VSCode's Remote Tunnels.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/iansyahr/vsctunnel",
    author="Muhamad Apriansyah Ramadhan",
    author_email="secret@example.com",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)

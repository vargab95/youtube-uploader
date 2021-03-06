from setuptools import setup


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


setup(
    name="youtube_uploader",
    version="1.4.1",
    packages=["youtube_uploader", "youtube_uploader.webdriver"],
    install_requires=parse_requirements("requirements.txt"),
)

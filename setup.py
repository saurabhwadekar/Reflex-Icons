from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name = "reflex-icons",
    version = "1.0.2",
    author="Saurabh Wadekar [ INDIA ]",
    packages=["reflex_icons"],
    license="MIT",
    maintainer="Saurabh Wadekar",
    maintainer_email="saurabhwadekar420@gmail.com",
    keywords=["react icons","icons","reflex-icons","reflex"],
    description=" This library provides all icons of React-icons wrapped for ReFlex framework",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/saurabhwadekar/Reflex-Icons",
    include_package_data=True,
    install_requires=[
        "reflex",
    ],
)
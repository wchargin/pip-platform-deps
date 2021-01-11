import setuptools

import wchargin_platform_dep4


setuptools.setup(
    name="wchargin_platform_dep4",
    version=wchargin_platform_dep4.__version__.replace("-", ""),
    description="Test for platform-specific deps with fallback",
    author="William Chargin",
    author_email="wchargin@gmail.com",
    packages=["wchargin_platform_dep4"],
    install_requires=[],
    tests_require=[],
    license="Apache 2.0",
)

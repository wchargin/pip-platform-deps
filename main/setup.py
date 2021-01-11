import setuptools

import wchargin_platform_main4


setuptools.setup(
    name="wchargin_platform_main4",
    version=wchargin_platform_main4.__version__.replace("-", ""),
    description="Test for platform-specific deps with fallback",
    author="William Chargin",
    author_email="wchargin@gmail.com",
    packages=["wchargin_platform_main4"],
    install_requires=["wchargin_platform_dep4"],
    tests_require=["wchargin_platform_dep4"],
    license="Apache 2.0",
)

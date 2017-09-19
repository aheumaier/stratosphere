from setuptools import setup

setup(
    name='stratosphere',
    version='0.0.1',
    description="Azure Template creation library",
    author="Andreas Heumaier",
    author_email="andreas.heumaier@microsoft.com",
    url="https://github.com/aheumaier/stratosphere",
    license="MIT",
    packages=['stratosphere', 'stratosphere.helpers'],
    scripts=['scripts/tmpl' ],
    test_suite="tests",
    tests_require=[],
    extras_require={},
    use_2to3=True,
)
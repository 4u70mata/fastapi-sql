from setuptools import setup, find_packages

setup(
    name="sql-fastapi",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi[all]",
        "sqlalchemy",
    ],
    entry_points={
        'console_scripts': [
            'start-app = main:app',  # Adjust if needed
        ],
    },
    author="4u70mata",
    description="A FastAPI project with SQLAlchemy",
    license="MIT",
    keywords="fastapi sqlalchemy",
)

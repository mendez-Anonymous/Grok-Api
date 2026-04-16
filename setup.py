from setuptools import setup, find_packages

setup(
    name="grok-api",
    version="2.0.0",
    author="Josué Méndez",
    author_email="umjosue0891@gmail.com",
    description="A professional Grok AI API wrapper - No authentication required",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "curl_cffi",
        "beautifulsoup4",
        "pydantic",
        "colorama",
        "coincurve",
        "requests",
    ],
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
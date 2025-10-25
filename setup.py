"""Setup configuration for reddit-scraper package"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="reddit-scraper",
    version="1.0.0",
    author="reddit-scraper contributors",
    description="Lightweight Reddit thread scraper with full comment hierarchy. FREE, fast, 100% extraction.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YOUR_USERNAME/reddit-scraper",  # Update after GitHub repo created
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
    ],
    python_requires=">=3.8",
    install_requires=[
        "fastapi>=0.100.0",
        "uvicorn>=0.20.0",
        "pydantic>=2.0.0",
        "requests>=2.28.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "reddit-scraper=reddit_scraper.scraper:main",
            "reddit-scraper-server=reddit_scraper.server:main",
        ],
    },
    include_package_data=True,
    keywords="reddit scraper api fastapi web-scraping comments hierarchy",
    project_urls={
        "Bug Reports": "https://github.com/YOUR_USERNAME/reddit-scraper/issues",
        "Source": "https://github.com/YOUR_USERNAME/reddit-scraper",
    },
)

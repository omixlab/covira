from setuptools import setup, find_packages
setup(
    name="covira",
    version="0.1.1",
    packages=find_packages(),

    install_requires=["numpy", "pandas"],

    author="Frederico Schmitt Kremer",
    author_email="fred.s.kremer@gmail.com",
    description="CoVIRA (Consensus by Voting with Iterative Re-weighting based on Agreement)",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords="bioinformatics machine-learning data science",
    project_urls={
        "Source Code": "https://github.com/fredericokremer/covira"
    }
)
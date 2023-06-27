from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

# Setting up
setup(
        name="anova_analysis", 
        version="0.0.1.1",
        authors=['Sarath S', 'Saranyadevi S'],
        author_email="insightagri10@gmail.com",
        description="A package for performing various ANOVA analysis",
        license='MIT',
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        packages=find_packages(),
        url="https://github.com/Insight-deviler/anova_analysis",
        install_requires=["tabulate", "pandas", "scipy",'numpy','math','warnings'],
        keywords=['Genetics and Plant breeding','Quantitative Genetics', 'ANOVA', 'Two-way ANOVA', 'RBD', 'CRD', 'One-Way ANOVA', 'analysis of variance'],
        classifiers= [
             "Programming Language :: Python :: 3",
             "License :: OSI Approved :: MIT License",
             "Operating System :: OS Independent",],
        python_requires = ">=3.6"
)
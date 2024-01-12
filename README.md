# Brabant Water Capstone project

## Setup
For all jupyter notebooks without a pyproject.toml file, conda/mamba has been used. Using Mamba is recommended as it is significantly faster than Conda. When installing mamba, conda is also installed since some commands are not usable in mamba. https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html

For most notebooks an environment can be created with these packages:
```
mamba create -n bd python=3.11 ipywidgets ipykernel pyarrow openpyxl pandas matplotlib numpy scipy seaborn geopandas shapely scikit-learn
mamba activate bd
mamba install -c conda-forge scikit-learn-intelex
```

Scikit-learn-intelex is a library that makes scikit-learn faster for x86_64 processors (not just Intel processors).For more information about scikit-learn-intelex, check out this [page](https://intel.github.io/scikit-learn-intelex/latest/quick-start.html).

Pyarrow adds support to pandas for Parquet files, openpyxl for Excel.

All other projects use [Poetry](https://python-poetry.org/).

Download the neerslag_ai folder from Teams and unpack it as follows:
![Alt text](image.png)

# Start- en stopppeilen van de gemalen
Hierbij de code voor radar naar zuiveringseenheden, en hieronder start- stoppeilen van de gemalen. De Bassins worden leeggepompt als stelsel leeg is.

RUC0001             Start      7,1 mNAP           Stop      6,6 mNAP
RUC0008             Start      5,6 mNAP           Stop      5,2 mNAP
RUC0013             Start      6,35 mNAP         Stop      6 mNAP
RUC0014             Start      4,26 mNAP         Stop       3,28 mNAP
RUC0015             Start      4,58 mNAP         Stop      3,94 mNAP
RUC0027             Start      6,1 mNAP           Stop       5,6 mNAP
RUC0030             Start      4,35 mNAP         Stop      4,1 mNAP

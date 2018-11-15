# Cara Menginstall Anaconda (versi Windows)

1. Download Anaconda di website resmi dari Anaconda : https://www.anaconda.com/download
2. Pilih versi yang ingin di download, contoh versi 37
3. Setelah selesai install package Anaconda.
4. Jalankan seperti menginstall pada software yang lainnya. 
5. Setelah selesai menginstall, maka akan muncul command prompt dari Anaconda
6. Kemudian masukkan "conda list" pada command prompt, nanti akan muncul hasil seperti dibawah

> `# packages in environment at C:\Users\Gucci Genk\Miniconda3:`<br>
`#`<br>
`# Name                    Version                   Build  Channel`<br>
`asn1crypto                0.24.0                   py37_0`<br>
`ca-certificates           2018.03.07                    0`<br>
`certifi                   2018.8.24                py37_1`<br>
`cffi                      1.11.5           py37h74b6da3_1`<br>
`chardet                   3.0.4                    py37_1`<br>
`conda                     4.5.11                   py37_0`<br>
`conda-env                 2.6.0                         1`<br>
`console_shortcut          0.1.1                         3`<br>
`cryptography              2.3.1            py37h74b6da3_0`<br>
`idna                      2.7                      py37_0`<br>
`menuinst                  1.4.14           py37hfa6e2cd_0`<br>
`openssl                   1.0.2p               hfa6e2cd_0`<br>
`pip                       10.0.1                   py37_0`<br>
`pycosat                   0.6.3            py37hfa6e2cd_0`<br>
`pycparser                 2.18                     py37_1`<br>
`pyopenssl                 18.0.0                   py37_0`<br>
`pysocks                   1.6.8                    py37_0`<br>
`python                    3.7.0                hea74fb7_0`<br>
`pywin32                   223              py37hfa6e2cd_1`<br>
`requests                  2.19.1                   py37_0`<br>
`ruamel_yaml               0.15.46          py37hfa6e2cd_0`<br>
`setuptools                40.2.0                   py37_0`<br>
`six                       1.11.0                   py37_1`<br>
`urllib3                   1.23                     py37_0`<br>
`vc                        14                   h0510ff6_3`<br>
`vs2015_runtime            14.0.25123                    3`<br>
`wheel                     0.31.1                   py37_0`<br>
`win_inet_pton             1.0.1                    py37_1`<br>
`wincertstore              0.2                      py37_0`<br>
`yaml                      0.1.7                hc54c509_2`<br>


# Cara Menginstall Airflow (versi Windows)
conda create -n airflow pip setuptools python=3.6
WARNING: A space was detected in your requested environment path
'C:\Users\Gucci Genk\Anaconda3\envs\airflow'
Spaces in paths can sometimes be problematic.
Solving environment: done

## Package Plan ##

  environment location: C:\Users\Gucci Genk\Anaconda3\envs\airflow

  added / updated specs:
    - pip
    - python=3.6
    - setuptools


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    wincertstore-0.2           |   py36h7fe50ca_0          13 KB
    python-3.6.7               |       h33f27b4_1        20.9 MB
    pip-18.1                   |           py36_0         1.8 MB
    wheel-0.32.2               |           py36_0          52 KB
    certifi-2018.10.15         |           py36_0         138 KB
    setuptools-40.5.0          |           py36_0         620 KB
    ------------------------------------------------------------
                                           Total:        23.5 MB

The following NEW packages will be INSTALLED:

    certifi:        2018.10.15-py36_0
    pip:            18.1-py36_0
    python:         3.6.7-h33f27b4_1
    setuptools:     40.5.0-py36_0
    vc:             14.1-h0510ff6_4
    vs2015_runtime: 14.15.26706-h3a45250_0
    wheel:          0.32.2-py36_0
    wincertstore:   0.2-py36h7fe50ca_0

Proceed ([y]/n)? y


Downloading and Extracting Packages
wincertstore-0.2     | 13 KB     | ############################################################################################################################ | 100%
python-3.6.7         | 20.9 MB   | ############################################################################################################################ | 100%
pip-18.1             | 1.8 MB    | ############################################################################################################################ | 100%
wheel-0.32.2         | 52 KB     | ############################################################################################################################ | 100%
certifi-2018.10.15   | 138 KB    | ############################################################################################################################ | 100%
setuptools-40.5.0    | 620 KB    | ############################################################################################################################ | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate airflow
#
# To deactivate an active environment, use
#
#     $ conda deactivate


(base) C:\Users\Gucci Genk>conda activate airflow

(airflow) C:\Users\Gucci Genk>conda deactivate


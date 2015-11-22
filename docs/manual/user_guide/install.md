
# Install NILMTK

### Install on Ubuntu like Linux variants (debian based) or OSX

NB: The following procedure is for Ubuntu like Linux variants (debian based). Please adapt accordingly for your OS. We would welcome installation instructions for other OSes as well.

We recommend using [Anaconda](https://store.continuum.io/cshop/anaconda/), which bundles togther most of the required packages. Please download Anaconda for Python 2.7.x. We do not currently support Python 3.

After installing Anaconda, please do the following:

- Update anaconda
```bash
conda update --yes conda
```

- Install system dependencies
```bash
sudo apt-get install git python-dev libhdf5-serial-dev
```

- Install psycopg2
First you need to install Postgres:
```bash
sudo apt-get install postgresql postgresql-contrib
sudo apt-get install postgresql-server-dev-all
```

- Finally! Install NILMTK
```bash
git clone https://github.com/nilmtk/nilmtk.git
cd nilmtk
python setup.py develop
cd..
```

- If you wish, you may also run NILMTK tests to make sure the installation has succeeded.
```bash
cd nilmtk
nosetests
```

### Install on Windows

- Install [Anaconda](https://store.continuum.io/cshop/anaconda/), which bundles togther most of the required packages. Please download Anaconda for Python 2.7.x. We do not currently support Python 3.

- Install [git](http://git-scm.com/download/win) client. You may need to add `git.exe` to your path in order to run nilmtk tests.

- Install pip and other dependencies which might be missing from Anaconda
```bash
conda install --yes pip numpy scipy six scikit-learn pandas numexpr pytables dateutil matplotlib networkx hmmlearn
```

-  Install postgresql support (currently needed for WikiEnergy converter)
Download release for your python environment:
http://www.stickpeople.com/projects/python/win-psycopg/

- Finally! Install nilmtk from git bash
```bash
git clone https://github.com/nilmtk/nilmtk.git
cd nilmtk
python setup.py develop
cd..
```

- If you wish, you may also run NILMTK tests to make sure the installation has succeeded
```bash
cd nilmtk
nosetests
```

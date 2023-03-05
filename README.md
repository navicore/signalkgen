Generate Test Data for Navactor
==============

NOTE: UNDER CONSTRUCTION - NOT VALID SIGNAL K DATA YET
==============

Data will eventually be signal k format and generate a time-series graph of
marine reporters reporting their own info as well as that of their nearest
neighbors'.


see: https://signalk.org/specification/1.7.0/doc/data_model.html

also, long live PEP 621

Installing
-----------

virtualenv

```
python -m venv venv
source ./venv/bin/activate
python -m pip install --upgrade pip
```

```
python -m pip install signalkgen
```

Or install with "editing" mode from cloned repo for development of the code.

```
python -m pip install -e .
```

Usage
----------

```
signalkgen --num-boats 300 --nautical-miles 5
```

Generate Test Data for Navactor
==============

A test data generator for [Signal K](https://signalk.org/specification/1.7.0/doc/data_model.html) json forming time-series graphs of
marine reporters reporting their own info as well as that of their nearest
neighbors'.


see: https://signalk.org/specification/1.7.0/doc/data_model.html

Test output is validated against the Signal K scheme with the [Signal K project's validation tool](https://github.com/SignalK/specification).

also, long live PEP 621

Status
----------

* Generates arrays of boats moving in different directions at different speeds.

* Currently boats reporting other boats is random and the nearest neighbor
feature is not implemented yet.

![Fun Mutation of Dot Output](docs/boats3.png)


Installing
-----------

virtualenv

```
python -m venv venv
source ./venv/bin/activate
python -m pip install --upgrade pip
```

via [Pypi](https://pypi.org/project/signalkgen/)

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

Validation
-------------

See `tox.ini` or `.github/workflows/check.yml` for automated tests that invoke the Signal K validation tools.

```
git clone https://github.com/SignalK/specification
cd specification
npm install
signalkgen --num-boats 300 --nautical-miles 5 | ./bin/validate.js
```

![Fun Mutation of Dot Output](docs/boats1.png)

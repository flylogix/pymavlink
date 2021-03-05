[![Build Status](https://travis-ci.org/ArduPilot/pymavlink.svg?branch=master)](https://travis-ci.org/ArduPilot/pymavlink)
# Pymavlink
This is a Python implementation of the MAVLink protocol.
It includes a source code generator (generator/mavgen.py) to create MAVLink protocol implementations for other programming languages as well.
Also contains tools for analyzing flight logs.

# Documentation

Please see http://ardupilot.org/dev/docs/mavlink-commands.html for mavlink command reference.

For realtime discussion please see the pymavlink [Gitter channel](https://gitter.im/ArduPilot/pymavlink)

Examples can be found [in the repository](examples/) or in the [ArduSub book](https://www.ardusub.com/developers/pymavlink.html)


# Installation 

Pymavlink supports both Python 2 and Python 3.

The following instructions assume you are using Python 3 and a Debian-based (like Ubuntu) installation.

.. note::

   pymavlink assumes the command "python" is in your path.  Your distribution may provide a package such as "python-is-python3" to ensure that "python" is in your path.

## Dependencies

Pymavlink has several dependencies :

    - [future](http://python-future.org/) : for Python 2 and Python 3 interoperability
    - [lxml](http://lxml.de/installation.html) : for checking and parsing xml file 
    - python3-dev : for mavnative (or python-dev for Python 2)
    - a C compiler : for mavnative

Optional :
    - numpy : for FFT
    - pytest : for tests

### On Linux

lxml has some additional dependencies that can be installed with your package manager (here with `apt-get`) :

.. note::

   If you continue to use Python 2 you may need to change package names here (e.g. python3-dev => python-dev)

```bash
sudo apt-get install gcc python3-dev libxml2-dev libxslt-dev
```

Optional for FFT scripts and tests:

```bash
sudo apt-get install python3-numpy python3-pytest
```

Using pip you can install the required dependencies for pymavlink :

```bash
sudo python -m pip install --upgrade future lxml
```

### On Windows

Use pip to install future as for Linux.
lxml can be installed with a Windows installer from here : https://pypi.org/project/lxml


## Installation

### For users

It is recommended to install pymavlink from PyPI with pip, that way dependencies should be auto installed by pip.

```bash
sudo python -m pip install --upgrade pymavlink
```

#### Mavnative

By default, pymavlink will try to compile and install mavnative which is a C extension for parsing mavlink. Mavnative only supports mavlink1.
To skip mavnative installation and reduce dependencies like `gcc` and `python-dev`, you can pass `DISABLE_MAVNATIVE=True` environment variable to the installation command:

```bash
sudo DISABLE_MAVNATIVE=True python -m pip install --upgrade pymavlink
```

### For developers

From the pymavlink directory, you can use :

```bash
sudo MDEF=PATH_TO_message_definitions python -m pip install . -v
```

Since pip installation is executed from /tmp, it is necessary to point to the directory containing message definitions with MDEF. MDEF should not be set to any particular message version directory but the parent folder instead. If you have cloned from mavlink/mavlink then this is ```/mavlink/message_definitions``` . Using pip should auto install dependencies and allow you to keep them up-to-date. 

Or:

```bash
sudo python setup.py install
```


# License
---------

pymavlink is released under the GNU Lesser General Public License v3 or later.

The source code generated by generator/mavgen.py is available under the permissive MIT License.

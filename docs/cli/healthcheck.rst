``baseplate-healthcheck``
=========================

Baseplate services have well-defined health-check endpoints. The
``baseplate-healthcheck`` tool connects to a given service and checks these
endpoints to see if they're alive.

Command Line
------------

There are two required arguments on the command line: the protocol of the
service to check (``thrift`` or ``wsgi``) and the endpoint to connect to.

For example, to check a Thrift-based service listening on port 9090:

.. code-block:: console

   $ baseplate-healthcheck thrift 127.0.0.1:9090

or a WSGI (HTTP) service listening on a UNIX domain socket:

.. code-block:: console

   $ baseplate-healthcheck wsgi /run/myservice.sock

Results
-------

If the service is healthy, the tool will exit with a status code indicating
success (0) and print "OK!". If the service is unhealthy, the tool will exit
with a status code indicating failure (1) and print an error message explaining
what went wrong.

Usage
-----

This script can be used as part of a process to validate a server after
creation, or to check service liveliness for a service discovery system.

# wazo-sysconfd-client [![Build Status](https://jenkins.wazo.community/buildStatus/icon?job=wazo-sysconfd-client)](https://jenkins.wazo.community/job/wazo-sysconfd-client)

A python library to connect to wazo-sysconfd. HTTPS is used by default. Certificates are verified by default. To disable certificate verification, use the verify_certificate=False argument when instantiating the client.

Usage:

```python
from wazo_sysconfd import Client

c = Client('localhost', prefix=None, version=None, https=False)

# Update dhcp configuration
status = c.dhcpd_update()
```

## How to implement a new command

Someone trying to implement a new command to the client would have to implement a new class, sub-classing the RESTCommand (available in wazo-lib-rest-client). The new class must be in the setup.py in the entry points under `sysconfd_client.commands`. The name of the entry point is used as the handle on the client. For example, if your new entry point entry looks like this:

```python
entry_points={
    'sysconfd_client.commands': [
        'foo = package.to.foo:FooCommand'
    ]
}
```

then your command will be accessible from the client like this:

```python
c = Client(...)

c.foo.bar()  # bar is a method of the FooCommand class
```

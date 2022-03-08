# wazo-sysconfd-client [![Build Status](https://jenkins.wazo.community/buildStatus/icon?job=wazo-sysconfd-client)](https://jenkins.wazo.community/job/wazo-sysconfd-client)

A python library to connect to wazo-sysconfd. HTTPS is used by default. Certificates are verified by default. To disable certificate verification, use the verify_certificate=False argument when instantiating the client.

Usage:

```python
from wazo_sysconfd import Client

c = Client('localhost', prefix=None, version=None, https=False)

# Update dhcp configuration
c.dhcpd_update()

# Move voicemail
c.move_voicemail()

# Delete voicemail
c.delete_voicemail()

# Generate common config
c.commonconf_generate()

# Apply common config
c.commonconf_apply()

# Exec request handlers (Asterisk, wazo-agentd, wazo-provd configuration)
body = {
    'ipbx': ['module reload something'],
    'chown_autoprov_config': [],
}
c.exec_request_handlers(body)

# Update hostname and hosts file
body = {
    'hostname': 'wazo',
    'domain': 'example.com',
}
c.hosts(body)

# Update resolv.conf
body = {
    'nameservers': ['192.168.0.1', '192.168.0.2'],
    'search': ['wazo.example.com', 'wazo.example.org'],
}
c.resolv_conf(body)

# Get HA config
config = c.ha_config.get(body)

# Update HA config
body = {
    'node_type': 'master',
    'remote_address': '192.168.99.99'
}
c.ha_config.update(body)

# Manage services
body = {
    'wazo-auth': 'start'
    'networking': 'restart'
    'wazo-confd': 'stop'
}
c.services(body)

# Check sysconfd status
status = c.status_check()

# Manage Wazo services
body = {
    'wazo-service': 'start',
}
c.xivoctl(body)
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

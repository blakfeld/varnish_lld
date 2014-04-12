## Varnish LLD

A Zabbix Low Level Discovery script for detecting:

  * What backends are in Varnish.
  * The health of those backends.
  * The ratio of how many backends are up/down.

### Install

On your Varnish server place both backend_health.py and lld_backend.py in:

```
/var/lib/zabbix/scripts/
```

Place userparameter_varnishbackends.conf in:

```
/etc/zabbix/zabbix_agentd.d/
```

Or copy it to the end of your Zabbix conf file. Then, just import the
Template_Varnish_Backend.xml file to your Zabbix server, and assign it to your
Varnish server.

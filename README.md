* based on https://github.com/gbagnoli/varnish-py, a ctype binding to the libvarnishapi1

* Simple configuration for collectd:

```
<Plugin python>
  ModulePath "/usr/lib/collectd/python"
  Import "collectd-varnish"
</Plugin>
```

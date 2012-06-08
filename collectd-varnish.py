#!/usr/bin/env python
import varnish
import collectd


def get_stats():
    with varnish.Instance() as v:
        v.stats.include('cache_hit')\
               .include('cache_miss')\
               .include('client_req')\
               .include('n_ban')\
               .include('n_vcl')\
               .include('backend_fail')\
               .include('shm_writes')\
               .include('shm_flushes')\
               .include('shm_records')\
               .include('shm_cycles')\
               .include('shm_cont')
	return v.stats.read().items()

def read(data=None):
    vl = collectd.Values(type='counter')
    for stat in get_stats():
        name, value = stat
        vl.plugin = 'varnish.' + name
        vl.dispatch(values=[value.value])

collectd.register_read(read, data=None)

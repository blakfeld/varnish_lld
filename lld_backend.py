#!/usr/bin/env python
"""

lld_backend.py - Parse out our backends, and send put it in
  zabbix friendly format for Low Level Discovery

"""

import json
import subprocess

def main():
  """
  Main
  """

  backends = subprocess.check_output("varnishadm debug.health | grep Backend | awk '{print $2}'", shell=True)
  backends = backends.replace('public_', '').replace('_ssl', '').split("\n")

  if len(backends) > len(set(backends)):
    backends = set(backends)

  data = list()
  for each_backend in backends:
    if each_backend:
      data.append({"{#BACKEND}":each_backend})

  print json.dumps({"data": data}, sort_keys=True, indent=4)


if __name__ == '__main__':
  main()

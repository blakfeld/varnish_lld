#!/usr/bin/env python
"""

backend_health.py - Return the health status
  of a specified varnish backend.

"""

import subprocess
from sys import exit, argv

def main(backend):
  """
  Main
  """

  health = subprocess.check_output("varnishadm debug.health | grep " +  backend + " | awk '{print $4}'", shell=True)
  health = set(health.split("\n"))

  if 'Sick' in health:
    print 'false'
  elif 'Healthy' in health
    print 'true'

if __name__ == "__main__":
  if not len(argv) > 1:
    print "You must specify a backend to check."
    exit(1)
  main(argv[1])

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import docker
import requests

client = docker.from_env()

time.sleep(10)
for c in client.containers.list():
    print(c.name)
    print(c.status)

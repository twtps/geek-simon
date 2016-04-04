#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function

import sys,os
import time,datetime
import pdb

def hello(name="world"):
	res =  "Hello %(name)s" %dict(name=name)
	return res

if __name__ == '__main__':
	a = hello("world!")
	print(a)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'chris8838'
__contact__ = 'lpkain@outlook.de'
__license__ = 'MIT'
__copyright__ = '(c) by Me!'
__version__ = '0.1.0'

import pyspeedtest

result = pyspeedtest.SpeedTest()
ping = result.ping(server='1.1.1.1')
calc = result.download()/1000000

metricsecond = "ms"
metricbandwith = "Mbit/s"
print ("Ping: " "%0.2f" % ping),
print metricsecond,
print ';',
print ("Download: " "%0.2f" % calc),
print metricbandwith


if __name__ == '__main__':
    pass
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4



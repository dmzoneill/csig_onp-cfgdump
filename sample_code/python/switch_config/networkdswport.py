#!/usr/bin/python

import os

from networkdfiles import Network
from networkdfiles import Link
from networkdfiles import Swport

# define a class
class NetworkdSwPort(Network, Link, Swport):

    def __init__(self, portname, dirname):
        self.name = portname
        self.dirname = dirname
        Swport.__init__(self, portname)
        Link.__init__(self, portname)
        Network.__init__(self, portname)

    def add_attrs(self, attrs):
        Swport.add_attrs(self, attrs)

    def add_qos(self, qos):
        Swport.add_qos(self, qos)

    def save_config(self):
        Swport.save_config(self, self.dirname)

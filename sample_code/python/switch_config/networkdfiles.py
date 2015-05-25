#!/usr/bin/python

import os

file_description = "# This file was generated after saving configuration"

# define a class
class Swport:

    section_match = '\n[Match]\n'
    section_swport_attrs = '\n[SWPortAttrs]\n'
    section_qos_attrs = '\n[QosAttrs]\n'

    def __init__(self, portname):
        self.match = {'Name': portname}
        self.file_extention = '.swport'
        self.attrs = {}
        self.qos = {}

    def add_attrs(self, attrs):
        self.attrs = attrs

    def add_qos(self, qos):
        self.qos = qos

    def save_config(self, dirname):

        if not os.path.exists(dirname):
            os.makedirs(dirname)

        swport_file = open(dirname+'/'+self.name+self.file_extention,'w')

        swport_file.write(file_description+"\n")

        swport_file.write(self.section_match)
        for key in self.match:
            swport_file.write(key+'='+self.match[key]+"\n")

        swport_file.write(self.section_swport_attrs)
        for key in self.attrs:
            swport_file.write(key[0]+'='+key[1]+"\n")

        swport_file.write(self.section_qos_attrs)
        for key in self.qos:
            swport_file.write(key[0]+'='+key[1]+"\n")

        swport_file.close()

class Link:
    def __init__(self, portname):
        self.match = {'Name': portname}

class Network:
    def __init__(self, portname):
        self.match = {'Name': portname}


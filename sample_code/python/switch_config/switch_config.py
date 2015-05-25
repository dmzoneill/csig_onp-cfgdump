#!/usr/bin/python
import subprocess
import json
import sys
import getopt
import argparse

# locally created classes
from networkdswport import NetworkdSwPort

# Global variables
section_ports = 'Ports'
section_attrs = 'Attributes'
section_qos = 'QOS'


# Get switch configuration from ohai
def switch_get_ohai_config():
    ohai_config = subprocess.check_output("ohai intel_switch", shell=True)
    python_config = json.loads(ohai_config)
    return python_config


def switch_save_one(port_name, port_val, dirname):
    port = NetworkdSwPort(port_name, dirname)

    # get port attributes
    attrs = port_val.get(section_attrs)
    port.add_attrs(attrs)

    # get port QOS attributes
    qos = port_val.get(section_qos)
    port.add_qos(qos)

    port.save_config() 


# Save switch configuration in networkd format
def switch_save_config_networkd(python_config, args):
    switch_ports = python_config.get(section_ports)

    if args.dev == 'all':
        for port_name in switch_ports:
            port_val = python_config[section_ports][port_name]
            switch_save_one(port_name, port_val, args.dirname)

    else:
        if args.dev in switch_ports:
            port_val = python_config[section_ports][args.dev]
            switch_save_one(args.dev, port_val, args.dirname)
        else:
            print "Port "+args.dev+" was not found"


def switch_save_config(args):
    python_config = switch_get_ohai_config()

    if args.format == 'networkd':
        switch_save_config_networkd(python_config, args)


#def switch_show_config(args):
#    print "Not yet implemented"
    

def get_args(argv):
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(help="subparsers")

    # create parser for "save"
    parser_save = subparsers.add_parser('save', help='Save switch configuration')
    parser_save.add_argument('-dirname', type=str, default='./switch_save_config/',
                             help='Directory name to save config in')
    parser_save.add_argument('-format', type=str, default='networkd', choices=['networkd'],
                             help='Output file format: networkd, chef')
    parser_save.add_argument('-dev', type=str, help='Switch port name', default='all')
    parser_save.set_defaults(func=switch_save_config)

    # create parser for "show"
#    parser_show = subparsers.add_parser('show', help='Show switch configuration')
#    parser_show.add_argument('-dev', type=str, help='Switch port name', default='all')
#    parser_show.add_argument('-feature', type=str, default='all', choices=['all', 'qos', 'attributes'],
#                             help='Feature to show information for')
#    parser_show.set_defaults(func=switch_show_config)

    #parse the args
    args = parser.parse_args()
    return args



def main(argv):
    args = get_args(argv)
    args.func(args)


if __name__ == '__main__':
    main(sys.argv[1:])


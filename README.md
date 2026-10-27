# csig_onp-cfgdump

Sample code for dumping the configuration of an Intel Ethernet switch
used with the Intel Open Network Platform (ONP).

## What it does

`sample_code/python/switch_config` reads the switch configuration with
`ohai intel_switch` and writes it out as systemd-networkd files: ports,
attributes and QoS settings for each switch port, saved as
`.network`, `.link` and `.swport` files.

## Tech

- Python
- Ohai and systemd-networkd

## Running

Run `switch_config.py` on a host where `ohai` and the
`intel_switch` plugin are installed.

## License

Licensed under the Apache License 2.0. See [LICENSE](LICENSE).

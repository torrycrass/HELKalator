# HELKalator

This project (HELKalator = [HELK + escalator]) contains a collection of scripts put together with the intent to make importing files into the HELK (and likely ELK) platforms somehow simpler.

Contribution to this project is welcomed.

## Scripts Present
- **Chop.PY** is a script meant to parse a monolithic Zeek/Bro file into its component files such conn.log and dns.log
- **parsley** is a script that takes two separate arrays, one with terms to find and a corresponding value in a second array and runs a search for terms in the first array and replaces those findings with corresponding terms in the second array while then writing out a new file with the overall results.

### TODO / NEEDED

- Guidance documentation created on how to import flat files into HELK/ELK instances via logstash, elasticsearch, and filebeat.

### Links to Additional Tools
I have used the json-py-es tool below with mixed results.
[json-py-es](https://github.com/xros/jsonpyes) : Software to import JSON to elasticsearch


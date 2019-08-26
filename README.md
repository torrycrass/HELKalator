[![](https://img.shields.io/badge/Chop.PY-released-green)](https://github.com/torrycrass/HELKalator/tree/master/chop.py/)
[![](https://img.shields.io/badge/parsely-released-green)](https://github.com/torrycrass/HELKalator/tree/master/parsely)
[![](https://img.shields.io/badge/license-NMP-lightgrey)](http://www.torrycrass.com/nmp-license-v1-0/)


# HELKalator

This project (HELKalator = [HELK + escalator]) contains a collection of scripts put together with the intent to make importing files into the HELK (and likely ELK) platforms somehow simpler.

Beyond all else data to be ingested must be formatted properly. If this is not the case, errors and problems of all shapes and sizes will pop up.

Contribution to this project is welcomed.  

**NOTE:** Code updates are driven from a local gitlab repository. Until proper integration on both push and pull is worked out, updates to code will be pushed from the local gitlab repository.  

## Scripts Present
- **Chop.PY** is a script meant to parse a monolithic Zeek/Bro file into its component files such conn.log and dns.log
- **parsley** is a script that takes two separate arrays, one with terms to find and a corresponding value in a second array and runs a search for terms in the first array and replaces those findings with corresponding terms in the second array while then writing out a new file with the overall results.

## HowTo Documents
- **General Troubleshooting** has been started
- **HowTo: Kibana GUI Import** draft has been completed
- **HowTo: Elasticsearch Import** has been started
- **HowTo: Logstash Import** is not started
- **HowTo: CURL Import** is not started

### TODO / NEEDED

* [ ]  Create documentation on how to import flat files into HELK/ELK instances via logstash, elasticsearch, and filebeat. (for normal people)
* [ ]  Integrate wiki from gitlab to github
* [ ]  Integrate a pull from github to gitlab to allow for github native updates vs. having to recreate in gitlab
* [ ]  Add README.md to imports, Chop.PY, and parsely directories
* [ ]  Add instructions to elasticsearch import for import tools
* [ ]  Add scripts for JSON to NDJSON conversion
* [ ]  Add field update find and replace lists as usable example/sample data
* [ ]  Link Kibana GUI Import document into Elasticsearch Import document

### Links to Additional Tools

*  [json-py-es](https://github.com/xros/jsonpyes) / Software to import JSON to elasticsearch : I have used the json-py-es tool below with mixed results.  
*  [elasticsearch_loader](https://github.com/Moshe/elasticsearch_loader) / Software to import data to elasticsearch. Currently actively developed but initially no luck importing data.
*  [evtxtoelk](https://github.com/dgunter/evtxtoelk) / Software to import windows event logs into ELK.

# HELKalator

This project (HELKalator = [HELK + escalator]) contains a collection of scripts put together with the intent to make importing files into the HELK (and likely ELK) platforms somehow simpler.

Contribution to this project is welcomed.

NOTE: Code updates are driven from a local gitlab repository. Until proper integration on both push and pull is worked out, updates to code will be pushed from the local gitlab repository.

## Scripts Present
- **Chop.PY** is a script meant to parse a monolithic Zeek/Bro file into its component files such conn.log and dns.log
- **parsley** is a script that takes two separate arrays, one with terms to find and a corresponding value in a second array and runs a search for terms in the first array and replaces those findings with corresponding terms in the second array while then writing out a new file with the overall results.

### TODO / NEEDED

* [ ]  Create documentation on how to import flat files into HELK/ELK instances via logstash, elasticsearch, and filebeat. (for normal people)
* [ ]  Integrate wiki from gitlab to github
* [ ]  Integrate a pull from github to gitlab to allow for github native updates vs. having to recreate in gitlab

### Links to Additional Tools

*  [json-py-es](https://github.com/xros/jsonpyes) / Software to import JSON to elasticsearch : I have used the json-py-es tool below with mixed results.  


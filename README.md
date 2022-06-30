# hl7_lis
This is an attempt to create bidirectional HL7 server.

It is mainly oriented to medical equipment communication

However, with modification , it should be possible to adapt other use

use mk_sample.py to create sample

use socat to communicate
```
socat file:hl7.sample tcp:127.0.0.1:2575
```
the responce will also be written in hl7.sample 

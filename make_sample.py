#!/usr/bin/python3
f=open("sample_hl7","w");
msg='MSH|^~\&|LIS|Example|Hospital|Mirth|20111207105244||ACK^A01|A234244|P|2.3.1';
hl7_msg=chr(11)+msg+chr(28)+chr(13)
f.write(hl7_msg)

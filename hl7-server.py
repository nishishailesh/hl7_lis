#!/usr/bin/python3
from hl7.mllp import start_hl7_server
import asyncio
 
async def process_hl7_messages(hl7_reader, hl7_writer):
    peername = hl7_writer.get_extra_info("peername")
    print(f"Connection established {peername}")
    try:
        while not hl7_writer.is_closing():
            hl7_message = await hl7_reader.readmessage()
            print(f'Received message\n {hl7_message}'.replace('\r', '\n'))
            # Now let's send the ACK and wait for the
            # writer to drain
            hl7_writer.writemessage(hl7_message.create_ack())
            await hl7_writer.drain()
    except asyncio.exceptions.IncompleteReadError:
        # Oops, something went wrong, if the writer is not
        # closed or closing, close it.
        if not hl7_writer.is_closing():
            hl7_writer.close()
            await hl7_writer.wait_closed()
    print(f"Connection closed {peername}")

async def main():
  hl7_server=await start_hl7_server(process_hl7_messages, port=2575)
  await hl7_server.serve_forever()
  
loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(main()),
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


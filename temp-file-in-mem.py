import io

# create a temp file in memory for fast IO.
# Use it as a queue/buffer, building a stream, holding text for
# processing later, etc.  Depending on your use case, io also
# hosts a io.BytesIO() option that works similarly for binary data.
tmpfileinmem = io.StringIO()

try:
    # Do your useful work here, stuffing data into the in-memory tmp file.
    tmpfileinmem.write("first string\n")
    tmpfileinmem.write("middle string\n")
    tmpfileinmem.write("last string\n")
    # Rewind the file before reading it (think C/C++ approach)
    tmpfileinmem.seek(0)
    # Ingest the tmp data using .read() and do something with it.
    print(f"{tmpfileinmem.read()}")
finally:
    # Always close the tmp file
    tmpfileinmem.close()
    
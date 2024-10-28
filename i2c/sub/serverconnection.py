from .webpage import main_homepage, data_page
from .filestorage import HTML
import utime

timeout = 10000

# Get a connection
# --------------------------------------------------
async def serve_client(reader, writer):
    print("client connected")
    request_line = await reader.readline()
    request_line = str(request_line, 'UTF-8')
    print("request ", request_line)
    
    if request_line.find('/log') != -1:
        response = HTML("log")
    elif request_line.find('/safe') != -1:
        response = HTML("safe")
    elif request_line.find('/data') != -1:
        response = data_page()
    else:
        response = main_homepage()
    
    # We are not interested in HTTP request headers, skip them
    starttime = utime.ticks_ms()
    while await reader.readline() != b"\r\n":
        if (utime.ticks_ms() - starttime) >= timeout: break
        else: pass
    #await reader.read(256)
    #await reader.read(1024)
    #while await reader.readline():
    #    pass
    
    writer.write('HTTP/1.1 200 OK\r\nContent-type: text/html\r\n\r\n')
    writer.write(response)
    
    await writer.drain()
    await writer.wait_closed()
    print("client disconnected")
    
    return writer

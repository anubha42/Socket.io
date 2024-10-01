import socketio
import os
import random
import time


sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': './ass_public/'
})


# Initialize counters
client_count = 0
room_count_a = 0
room_count_b = 0
counter = 0

# Handle client connection
@sio.event
def connect(sid, environ):
    print(sid, 'connected')

# Handle client disconnection
@sio.event
def disconnect(sid):
    print(sid, 'disconnected')

# Handle 'start_counter' event
@sio.event
def start_counter(sid, data):
    print(f"Received from {sid}: {data}")
    counter = 0 
    while True:
        sio.sleep(2)  # Sleep for 1 second
        counter += 1
        result = counter
        # Send counter value to the client
        sio.emit('counter_update', result, to=sid)
        print(f"Sent {result} to {sid}")

        


    
    
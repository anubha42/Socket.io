import socketio
import os
import random
import time
import os  # Add the missing os import
import socketio


# Create a Socket.IO server instance
sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': './public/'
})

# Initialize counters
client_count = 0  # Fixed spelling from clinet_count
room_count_a = 0
room_count_b = 0
counter = 0

# Handle client connection
@sio.event
def connect(sid, environ):
    global client_count, room_count_a, room_count_b
    global counter
    client_count += 1
    print(sid, 'connected')

    # Randomly assign to room 'a' or 'b'
    if random.random() > 0.5:
        sio.enter_room(sid, 'a')
        room_count_a += 1
        sio.emit('room_count', room_count_a, to='a')
    else:
        sio.enter_room(sid, 'b')
        room_count_b += 1
        sio.emit('room_count', room_count_b, to='b')


    # Emit the updated client count
    sio.emit('client_count', client_count)

# Handle client disconnection
@sio.event
def disconnect(sid):
    global client_count, room_count_a, room_count_b
    client_count -= 1
    print(sid, 'disconnected')

    # Update room counts
    if 'a' in sio.rooms(sid):
        room_count_a -= 1
        sio.emit('room_count', room_count_a, to='a')
    else:
        room_count_b -= 1
        sio.emit('room_count', room_count_b, to='b')

    # Emit the updated client count
    sio.emit('client_count', client_count)

# Handle sum event
@sio.event
def counter(sid,data):
    while True:
        sio.sleep(1)
        print(data['count'])
        data['count'][0] = data['count'][0]+1
        result = data['count'][0]
        return result





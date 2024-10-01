import socketio
import eventlet
import os


sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': './ass2_public/message.html'
})

# Handle client connection
@sio.event
def connect(sid, environ):
    sio.enter_room(sid, 'a')  # Add the client to room 'a'
    print(f'{sid} connected')
    sio.emit('display_message', f'User {sid} has connected!', room='a')

# Handle client disconnection
@sio.event
def disconnect(sid):
    print(f'{sid} disconnected')
    sio.emit('display_message', f'User {sid} has disconnected!', room='a')

# Handle 'message' event
@sio.event
def message(sid, data):
    print(f"Received message from {sid}: {data}")
    # Broadcast the message to everyone in room 'a'
    sio.emit('display_message', f'{sid}: {data}', room='a')


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 8000)), app)

        


    
    









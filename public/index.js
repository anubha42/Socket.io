const sio = io();

sio.on('connect', () => {
    console.log('connected');
    sio.emit('counter',{'count': [0, 1]}, (result) => {
        console.log(result)

    })
});

sio.on('disconnect', () => {
    console.log('disconnected');
});


sio.on('client_count', (client_count) => {
    console.log('there are ' + client_count + ' clients.');
    document.getElementById('client-count').textContent = 'There are ' + client_count + ' clients connected.';
});

sio.on('room_count', (room_count) => {
    console.log('there are ' + room_count + ' clients in my room.');
    document.getElementById('room-count').textContent = 'There are ' + room_count + ' clients in my room.';
});



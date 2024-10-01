const sio = io();

sio.on('connect', () => {
    console.log('connected');

    sio.emit('start_counter', 'hi');

});

sio.on('counter_update', (counter) => {
    console.log('Counter update received:', counter);
    document.getElementById('count').textContent = 'Counter: ' + counter;
});



sio.on('disconnect', () => {
    console.log('disconnected');
});

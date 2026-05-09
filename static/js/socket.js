const socket = io();

socket.on("connect", function() {
    console.log("Connected to WebSocket server")
});

socket.on('task_updated', function (data) {
  if (typeof window.onTaskUpdated === 'function') {
    window.onTaskUpdated();
  }
});
const socket = io();

socket.on("connect", function() {
    console.log("Connected to WebSocket server")
});

socket.on("task_updated", function (data) {
console.log("Task changed:", data);
})
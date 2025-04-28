function sendMessage() {
    const input = document.getElementById("chatInput");
    const chatWindow = document.getElementById("chatWindow");
    const message = input.value.trim();

    if (message === "") return;

    // Show user message
    chatWindow.innerHTML += `<div class="chat-message user"><strong>You:</strong> ${message}</div>`;

    // Send to Flask server
    fetch('/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `question=${encodeURIComponent(message)}`
    })
    .then(response => response.json())
    .then(data => {
        chatWindow.innerHTML += `<div class="chat-message bot"><strong>MedBot:</strong> ${data.answer}</div>`;
        chatWindow.scrollTop = chatWindow.scrollHeight;
    });

    input.value = "";
}

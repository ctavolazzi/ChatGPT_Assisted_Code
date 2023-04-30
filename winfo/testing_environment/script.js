// scripts.js
$(document).ready(function () {
    $("#chat-form").on("submit", function (event) {
        event.preventDefault();
        const userInput = $("#user-input").val().trim();
        if (userInput) {
            sendMessage(userInput);
            $("#user-input").val("");
        }
    });

    $("#reset-btn").on("click", function () {
        resetChat();
    });
});

function sendMessage(userInput) {
    $.post("/chat", { user_input: userInput }, function (data) {
        const assistantReply = data.assistant_reply;
        displayMessage(userInput, "user");
        displayMessage(assistantReply, "assistant");
        updateScroll();
    });
}

function displayMessage(message, role) {
    const messageElement = $("<div>").addClass(role + "-message").text(message);
    $("#chat-container").append(messageElement);
}

function updateScroll() {
    const chatContainer = $("#chat-container");
    chatContainer.scrollTop(chatContainer[0].scrollHeight);
}

function resetChat() {
    $.post("/reset", function (data) {
        if (data.reset) {
            $("#chat-container").empty();
            location.reload();
        }
    });
}

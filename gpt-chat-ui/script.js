let editingMessage = null;
let editMode = false;

function sendMessage() {
  const userInput = document.getElementById("user-input").value;
  if (!userInput) {
    return;
  }

  const chatBox = document.getElementById("chat-box");
  const message = document.createElement("div");
  message.classList.add("chat-message");
  message.textContent = userInput;

  if (editMode && editingMessage) {
    editingMessage.textContent = userInput;
    editMode = false;
    editingMessage.classList.remove("selected");
    editingMessage = null;
  } else {
    chatBox.appendChild(message);
    chatBox.scrollTop = chatBox.scrollHeight;
  }

  document.getElementById("user-input").value = "";
}

function editMessage() {
  const userInput = document.getElementById("user-input");
  const selectedMessage = document.querySelector(".chat-message.selected");
  if (selectedMessage) {
    editingMessage = selectedMessage;
    editMode = true;
    userInput.value = selectedMessage.textContent;
  }
}

function copyText() {
  const selectedMessage = document.querySelector(".chat-message.selected");
  if (selectedMessage) {
    navigator.clipboard.writeText(selectedMessage.textContent);
  }
}

function saveAndSubmit() {
  const chatMessages = document.querySelectorAll(".chat-message");
  const messages = Array.from(chatMessages).map(message => message.textContent);
  // You can do something with the messages, like submit them to a server
  console.log("Messages to submit:", messages);
}

function cancelEdit() {
  editingMessage = null;
  editMode = false;
  document.getElementById("user-input").value = "";
}




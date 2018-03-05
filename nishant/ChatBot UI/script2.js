function sendMsg() {
  var msg = document.getElementById("msg").value;
  if (msg.replace(/\s/g, '').length) {
    msg = msg.replace(/\r?\n/g, '<br/>');
    var new_msg = `<div class="chat self">
                      <div class="user-photo"><img src="man.png"></div>
                      <p class="chat-message">${msg}</p>
                  </div>`;
    document.getElementById("chat_logs").innerHTML += (new_msg);
  }
  document.getElementById("msg").value = "";
}
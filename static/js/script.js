// Export function when testing with Jest
module.exports = removeFlashMessage;

// Remove flash message alert
document.addEventListener("DOMContentLoaded", removeFlashMessage);

function removeFlashMessage() {
  setTimeout(function () {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
  }, 3000);
}

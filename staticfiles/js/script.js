// w3s modal https://www.w3schools.com/howto/howto_css_modals.asp
// Get the modal
const modal = document.getElementById("myModal");

// Get the button that opens the modal
const buttons = document.getElementsByClassName("my-btn");

// Get the <span> element that closes the modal
const close = document.getElementsByClassName("modal--close");

// When the user clicks on the button, open the modal
for (let button of buttons) {
    button.onclick = function () {
        modal.style.display = "block";
    }
}

// When the user clicks on cancel or (x), close the modal
for (let button of close) {
    button.onclick = function () {
        modal.style.display = "none";
    }
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// code from code institue thorin & company flask 
document.addEventListener("DOMContentLoaded", function () {
    let copyRightDate = document.getElementsByClassName("copyright-date");
    for (let items of copyRightDate){
        items.textContent = new Date().getFullYear();
    }
});

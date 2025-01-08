const channel = document.getElementsByClassName("channel");
const channelList = document.getElementById("channel-list");
const channelContent = document.getElementById("channel-content");

function displayChannel() {
    if (window.innerWidth < 576) {
        channelList.classList.add("d-none");
        channelContent.classList.remove("d-none");
        channelContent.classList.add("col-12");
    } else {
        channelList.classList.remove("d-none");
        channelContent.classList.add("d-none");
        channelContent.classList.remove("col-12");
    }
}

displayChannel()

// resize event https://www.w3schools.com/jsref/event_onresize.asp
window.addEventListener("resize", displayChannel);

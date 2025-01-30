const channelList = document.getElementById("channel-list");
const channelContent = document.getElementById("channel-content");


/**
 * shows the channel list as 'home'
 * on small devices less then 576px width
 * removes and adds bootstrap classes
 */
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


// calls the displayChannel function
displayChannel();

document.addEventListener("DOMContentLoaded", function () {
    // resize event https://www.w3schools.com/jsref/event_onresize.asp
    // calls the displayChannel function as screen is adjusted
    window.addEventListener("resize", displayChannel);
});

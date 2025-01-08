// code from w3s https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_sidenav_full
function openNav() {
    let open = document.getElementById("mySidenav");

    if (open.style.width === "70%") {
        document.getElementById("mySidenav").style.width = "0";
    } else if (window.innerWidth >= 576) {
        document.getElementById("mySidenav").style.width = "70%";
    } else {
        document.getElementById("mySidenav").style.width = "100%";
    }
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}

function menuButtonDisplay() {

    if (window.innerWidth >= 576) {
        document.getElementById("menu-button").innerHTML = "Menu";
    } else {
        document.getElementById("menu-button").innerHTML = "&#9776;";
    }
}

menuButtonDisplay()

// resize event https://www.w3schools.com/jsref/event_onresize.asp
window.addEventListener("resize", menuButtonDisplay);

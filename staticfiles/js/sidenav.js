// code from w3s https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_sidenav_full
function openNav() {
    let open = document.getElementById("mySidenav");

    if (open.style.width === "67%") {
        document.getElementById("mySidenav").style.width = "0";
    } else if (window.innerWidth >= 576) {
        document.getElementById("mySidenav").style.width = "67%";
    } else {
        document.getElementById("mySidenav").style.width = "100%";
    }
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}

function sideDisplay() {
    let menuButton = document.getElementById("menu-button");

    if (window.innerWidth >= 768) {
        menuButton.innerHTML = "Menu";
    } else {
        menuButton.innerHTML = `<i class="fa-solid fa-bars"></i>`;
    }
}

sideDisplay()

// resize event https://www.w3schools.com/jsref/event_onresize.asp
window.addEventListener("resize", sideDisplay);

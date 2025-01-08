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

function sideDisplay() {
    let menuButton = document.getElementById("menu-button");
    let sideHeader = document.getElementById("side-header");

    if (window.innerWidth >= 576) {
        menuButton.innerHTML = "Menu";
        sideHeader.innerHTML = `<i class="fa-solid fa-chart-line"></i>`;
    } else {
        menuButton.innerHTML = "&#9776;";
        sideHeader.innerHTML = `Crypto Net <i class="fa-solid fa-chart-line"></i>`;
    }
}

sideDisplay()

// resize event https://www.w3schools.com/jsref/event_onresize.asp
window.addEventListener("resize", sideDisplay);

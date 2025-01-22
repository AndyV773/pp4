// code from w3s https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_sidenav_full
/**
 * fuction for navigational menu
 * opens menu for large screens 67% of the width
 * closes menu for large devices
 * opens menu full width for smaller device less than 576px
 */
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


// function to close nav
function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}


/**
 * changes menu button inner html
 * diplay 'menu' on screen sizes 768px or greater
 * dispaly burger menu for smaller devices
 */
function sideDisplay() {
    let menuButton = document.getElementById("menu-button");
    if (window.innerWidth >= 768) {
        menuButton.innerHTML = "Menu";
    } else {
        menuButton.innerHTML = `<i class="fa-solid fa-bars"></i>`;
    }
}


// calls the sideDisplay function
sideDisplay()


// resize event https://www.w3schools.com/jsref/event_onresize.asp
// calls the sideDisplay function as screen is adjusted
window.addEventListener("resize", sideDisplay);

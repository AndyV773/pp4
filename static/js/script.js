// w3s modal https://www.w3schools.com/howto/howto_css_modals.asp
// w3s sidenave https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_sidenav_full
// Get the modal
const modal = document.getElementById("delete-modal");
// Get the button that opens the modal
const modalButtons = document.getElementsByClassName("btn-modal");
// Get the <span> element that closes the modal
const closeModal = document.getElementsByClassName("modal--close");
// sidenav buttons
const navOpenBtn = document.getElementById("sidenav-open");
const navCloseBtn = document.getElementById("sidenav-close");


/* When the user clicks on the button, open the modal
* - Displays a confirmation modal to prompt 
* the user for confirmation before deletion.
*/
for (let button of modalButtons) {
    button.onclick = function () {
        modal.style.display = "block";
    };
}


// When the user clicks on cancel or (x), close the modal
for (let button of closeModal) {
    button.onclick = function () {
        modal.style.display = "none";
    };
}


// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
};


/**
 * fuction for navigational menu
 * opens menu for large screens 67% of the width
 * closes menu for large devices
 * opens menu full width for smaller device less than 576px
 */
function openNav() {
    let sidenav = document.getElementById("the-sidenav");
    if (sidenav.style.width === "67%") {
        sidenav.style.width = "0";
    } else if (window.innerWidth >= 576) {
        sidenav.style.width = "67%";
    } else {
        sidenav.style.width = "100%";
    }
}


// function to close nav
function closeNav() {
    document.getElementById("the-sidenav").style.width = "0";
}


/**
 * changes menu button inner html
 * diplay 'menu' on screen sizes 768px or greater
 * dispaly burger menu for smaller devices
 */
function sideDisplay() {
    if (window.innerWidth >= 768) {
        navOpenBtn.innerHTML = "Menu";
    } else {
        navOpenBtn.innerHTML = `<i class="fa-solid fa-bars"></i>`;
    }
}


// calls the sideDisplay function
sideDisplay();


document.addEventListener("DOMContentLoaded", function () {

    // code from code institue thorin & company flask
    // gets current year and displays in the copyright text
    let copyRightDate = document.getElementsByClassName("copyright-date");
    for (let items of copyRightDate) {
        items.textContent = new Date().getFullYear();
    }

    // resize event https://www.w3schools.com/jsref/event_onresize.asp
    // calls the sideDisplay function as screen is adjusted
    window.addEventListener("resize", sideDisplay);

    navCloseBtn.addEventListener("click", closeNav);
    navOpenBtn.addEventListener("click", openNav);
});

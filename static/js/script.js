document.addEventListener("DOMContentLoaded", function () {
    let copyRightDate = document.getElementsByClassName("copyright-date");
    for (let items of copyRightDate){
        items.textContent = new Date().getFullYear();
    }
});

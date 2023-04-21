
// toggle menu visibility on button click
document.getElementById("menu-button").addEventListener("click", function() {
    document.getElementById("menu").classList.toggle("hidden");
});

// toggle level visibility on mode button click
var modeButtons = document.querySelectorAll(".mode-button");
for (var i = 0; i < modeButtons.length; i++) {
    modeButtons[i].addEventListener("click", function() {
        var levels = this.nextElementSibling;
        if (levels.classList.contains("hidden")) {
            levels.classList.remove("hidden");
        } else {
            levels.classList.add("hidden");
        }
    });
}

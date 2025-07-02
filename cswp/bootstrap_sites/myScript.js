document.addEventListener("DOMContentLoaded", () => {
    const button = document.querySelector("#hello");

    function myFunction() {
        document.querySelector(".demo").innerHTML = "<p>Paragraph has been modified by JavaScript</p>"
    }
    button.onclick = myFunction;
    window.alert("Hello World!");
    console.log("Welcome to my site.");
})
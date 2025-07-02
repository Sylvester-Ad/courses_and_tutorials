document.addEventListener("DOMContentLoaded", () => {
    const helloElement = document.getElementById("hello");
    if (helloElement) {
        helloElement.textContent = "Hello, World!";
        
    } else {
        console.error("Element with ID 'hello' not found.");
    }



    let value = 0;
    value += 1;
    console.log("Value incremented:", value); 


    
})
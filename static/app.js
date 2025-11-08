const form = document.getElementById("playerForm");
if (form) {
    form.addEventListener("submit", (e) => {
      // By default, submitting a form refreshes the page or data to a URL, 
      // but we want to stay on same page 
        e.preventDefault(); 
        const name = document.getElementById("pname").value.trim();
        if (name) {
            // Goes to card/html and adds the player's name to the URL
            window.location.href = `/static/card.html?name=${encodeURIComponent(name)}`;
        }
        
    } )
}
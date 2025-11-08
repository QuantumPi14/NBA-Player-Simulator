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

    // grabs the ?something=value, in this case it's ?name=NBA%20Player
    const params = new URLSearchParams(window.location.search);
    const Name = params.get("name");

    // Checks if there is a name in the URL and there's an element that has an ID cardContainer
    if (Name && document.getElementById("cardContainer")){
        loadPlayer(Name);
    }

    // Using async because this will probably take a while, don't wantn to hold up teh whole program to fetch the data.
    async function loadPlayer(name) {
        // Sends a GET request to ...
        const res = await fetch(`/api/player?name=${encodeURIComponent(name)}`);
        // Converts player data to json
        const data = await res.json();
        const container = document.getElementById("cardContainer");
        
        container.innerHTML = `
            <div class="card">
                <div class="stats">
                    <p><strong>PPG:</strong> ${data.ppg}</p>
                    <p><strong>RPG:</strong> ${data.rpg}</p>
                    <p><strong>APG:</strong> ${data.apg}</p>
                </div>
                <div class="name">${data.name}</div>
            </div>
        `;
    }
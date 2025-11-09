// Form submission handler for index page
const form = document.getElementById("playerForm");
if (form) {
    form.addEventListener("submit", (e) => {
        e.preventDefault(); 
        const name = document.getElementById("pname").value.trim();
        if (name) {
            window.location.href = `/static/stats.html?name=${encodeURIComponent(name)}`;
        }
    });
}

// Load player data onto page
const params = new URLSearchParams(window.location.search);
const playerName = params.get("name");

if (playerName && document.getElementById("playerStatsContainer")) {
    loadPlayer(playerName);
}

async function loadPlayer(name) {
    try {
        const res = await fetch(`/api/player?name=${encodeURIComponent(name)}`);
        const data = await res.json();
        const container = document.getElementById("playerStatsContainer");
        
        if (data.error) {
            container.innerHTML = `<div class="error">${data.error}</div>`;
            return;
        }
        
        const formatStat = (value) => {
            if (typeof value === 'number') {
                return value.toFixed(1);
            }
            return value || '0.0';
        };
        
        // So it only shows 3 decimal places instead of for example 0.5210000
        const formatPct = (value) => {
            if (typeof value === 'number') {
                return value.toFixed(3);
            }
            return value || '0.000';
        };
        
        container.innerHTML = `
            <h2 class="player-name">${data.name}</h2>
            <table class="stats-table">
                <thead>
                    <tr>
                        <th>PPG</th>
                        <th>RPG</th>
                        <th>APG</th>
                        <th>SPG</th>
                        <th>BPG</th>
                        <th>FG%</th>
                        <th>3PT%</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>${formatStat(data.ppg)}</td>
                        <td>${formatStat(data.rpg)}</td>
                        <td>${formatStat(data.apg)}</td>
                        <td>${formatStat(data.spg)}</td>
                        <td>${formatStat(data.bpg)}</td>
                        <td>${formatPct(data.fg_pct)}</td>
                        <td>${formatPct(data.fg3_pct)}</td>
                    </tr>
                </tbody>
            </table>
        `;
    } catch (error) {
        const container = document.getElementById("playerStatsContainer");
        container.innerHTML = `<div class="error">Error loading player data</div>`;
    }
}
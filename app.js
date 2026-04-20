const firebaseURL = "https://YOUR_PROJECT.firebaseio.com/";

function fetchData() {
  fetch(firebaseURL + ".json")
    .then(res => res.json())
    .then(data => {
      document.getElementById("moisture").innerText = data.moisture;
      document.getElementById("pump").innerText = data.pump;
    });
}

function togglePump() {
  fetch(firebaseURL + "/pump.json", {
    method: "PUT",
    body: JSON.stringify("ON")
  });
}

setInterval(fetchData, 2000);
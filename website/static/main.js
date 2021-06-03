
let form = document.querySelector("#user-text-form");

function postFormData(url, data, headers) {
    return fetch(url, {
        method: "POST",
        body: data,
        headers: headers
    })
    .then(response => response.json())
    .catch(error => console.log(error));
}



function buildResponse(response) {
    const answer = document.createElement("div")
    answer.classList.add("answer")

    const answerGranpyAddress = document.createElement("p");
    answerGranpyAddress.classList.add("answer-grandpy-address");
    answerGranpyAddress.textContent = response.grandpy_address

    answer.appendChild(answerGranpyAddress);

    const mapDiv = document.createElement("div")
    mapDiv.classList.add("map")
    mapDiv.setAttribute("id", "map");

    let map;

    function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: -34.397, lng: 150.644 },
        zoom: 8,
    });
    }

    var script = document.createElement('script');
    script.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyDv4_XB-nvhxiZU-vh70nohrUKqZLaQSPU&callback=initMap';
    script.async = true;

    window.initMap = function() {};

    mapDiv.appendChild(script);

    answer.appendChild(mapDiv);

    const conversationContainer = document.querySelector("#conversationContainer");
    conversationContainer.appendChild(answer);
}

form.addEventListener("submit", function(event) {
    event.preventDefault();
    
    postFormData("/grandpy", document.querySelector("#userText").value, {
        "Content-type": "plain/text"
    })
    .then(response => {
        buildResponse(response);
    })

})

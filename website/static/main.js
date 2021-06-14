
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

function buildQuestion(value) {
    const question = document.createElement("div")
    question.classList.add("question")
    question.textContent = value

    const conversationContainer = document.querySelector("#conversationContainer");
    conversationContainer.appendChild(question);
}

function initMap(latitude, longitude, address) {

    const answerMap = document.createElement("div");
    answerMap.classList.add("answer");
    answerMap.classList.add("answer-map");

    const place = {
        lat: latitude,
        lng: longitude
    };
    console.log(place)
    const map = new google.maps.Map(answerMap, {
        zoom: 12,
        center: place,
    });
    const marker = new google.maps.Marker({
        position: place,
        map: map,
        title: address
    });

    return answerMap
}

function buildResponse(response) {
    const answerHeader = document.createElement("div");
    answerHeader.classList.add("answer");
    answerHeader.setAttribute("id", "answer");
    answerHeader.textContent = response.grandpy_address + response.address;

    const answerMap = initMap(response.latitude, response.longitude, response.address)

    const answerWiki = document.createElement("div");
    answerWiki.classList.add("answer");
    answerWiki.setAttribute("id", "answer-wiki");
    answerWiki.textContent = response.grandpy_wiki;

    const answerWiki2 = document.createElement("div");
    answerWiki2.classList.add("answer");
    answerWiki2.setAttribute("id", "answer-wiki-2");
    answerWiki2.textContent = response.story;
    
    const seeFullStory = document.createElement("div");
    seeFullStory.classList.add("answer");
    seeFullStory.setAttribute("id", "seeFullStory");
    const span = document.createElement("span");
    const link = document.createElement("a");
    link.setAttribute('href', response.fullurl);
    link.setAttribute('target','_blank');
    link.textContent = "[Voir l'anecdote complète]";
    span.appendChild(link);
    seeFullStory.appendChild(link);
    
    const mapDiv = document.createElement("div");
    mapDiv.setAttribute("id", "mapDiv");
    mapDiv.appendChild(answerMap);
    const conversationContainer = document.querySelector("#conversationContainer");
    conversationContainer.appendChild(answerHeader);
    conversationContainer.appendChild(mapDiv);
    conversationContainer.appendChild(answerWiki);
    conversationContainer.appendChild(answerWiki2);
    conversationContainer.appendChild(seeFullStory);
}

function resetInputForm() {
    document.getElementById("userText").value = "";
};

function runLoadAnimation() {
    let inputButton = document.querySelector('#inputButton');
    inputButton.classList.add('spinning');
    setTimeout(() => inputButton.classList.remove('spinning'), 2000);
  };

form.addEventListener("submit", function(event) {
    event.preventDefault();

    runLoadAnimation();

    buildQuestion(document.querySelector("#userText").value)
    
    postFormData("/grandpy", document.querySelector("#userText").value, {
        "Content-type": "plain/text"
        })
        .then(response => {
            buildResponse(response)
        })
        .catch(error => console.log(error));

    resetInputForm();
})

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

form.addEventListener("submit", function(event) {
    event.preventDefault();
    
    postFormData("/grandpy", document.querySelector("#userText").value, {
        "Content-type": "plain/text"
    })
    .then(response => {
        console.log(response);
    })

})

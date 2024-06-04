let subscriberForm = document.getElementById('subscribe-form')
let subscribeMessage = document.getElementById('subscribe-message')
subscriberForm.addEventListener('submit', function(event){
    console.log("here");
    let email = document.getElementById('subscribe-email')
    event.preventDefault()
    fetch(`${location.origin}/api/subscriber/`, {
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : subscriberForm.csrfmiddlewaretoken.value
        },
        body: JSON.stringify({"email" : email.value})
    }).then(response => {
        if(response.ok) {
            subscribeMessage.innerHTML = `<h2>Thanks for your subscribe </h2>`
        }
        else{
            subscribeMessage.innerHTML = `<h2>This email has been used </h2>`
            alert('Error') 
        }
    })
})
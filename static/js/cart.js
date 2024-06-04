const addToCartBtn1 = document.getElementsByClassName('addToCart')
console.log(addToCartBtn1);
for(var i=0;i<addToCartBtn1.length;i++){
    addToCartBtn1[i].addEventListener('click',function(event){
        const quantity=document.querySelector("input[name='qtybutton']")
        console.log(event.target.dataset.product);
        event.preventDefault()
        fetch(`${location.origin}/api/order-items/`, {
            method: 'POST',
            headers : {
                'Content-Type' : 'application/json',
                'X-CSRFToken' : subscriberForm.csrfmiddlewaretoken.value
            },
            body : JSON.stringify({"product":event.target.dataset.product})
        }).then(response => {
            if (response.ok)  {
                subscribeMessage.innerHTML = `<h2>Thanks for subscribing!</h2>`;
            }
            else {
                throw new Error('Network response was not ok');
            }
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
            alert('Error');
        });
    });
} 
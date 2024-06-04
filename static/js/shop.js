const addToWishlistBtns = document.getElementsByClassName('addToWishlist');
console.log(addToWishlistBtns);


for (var i = 0; i < addToWishlistBtns.length; i++) {
    addToWishlistBtns[i].addEventListener('click', function (event) {
        console.log(event.target.dataset.product);
        
        event.preventDefault();
        fetch(`${location.origin}/api/wishlist/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': subscriberForm.csrfmiddlewaretoken.value
            },
            body: JSON.stringify({ "product": event.target.dataset.product })
        }).then(response => {
            if (response.ok) {
                alert('Item added to wishlist successfully!');
            } else {
                throw new Error('Network response was not ok');
            }
        })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
                alert('Error');
        });
    });
}
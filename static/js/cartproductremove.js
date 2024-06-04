<script>
    document.addEventListener("DOMContentLoaded", function() {
        // Find all remove buttons
        var removeButtons = document.querySelectorAll('.remove-item');
        
        // Attach click event listener to each remove button
        removeButtons.forEach(function(button) {
            button.addEventListener('click', function(event) {
                event.preventDefault(); // Prevent default link behavior
                var productId = this.getAttribute('data-product-id');
                
                // Send an AJAX request to the server to remove the item
                fetch('/remove-from-cart/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'X-CSRFToken': '{{ csrf_token }}'  // Include CSRF token
                    },
                    body: 'product_id=' + encodeURIComponent(productId)
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        // Item removed successfully, you can update the UI here
                        // For example, remove the row from the table
                        button.closest('tr').remove();
                        // Update the subtotal
                        updateSubtotal(data.subtotal);
                    } else {
                        console.error('Failed to remove item');
                    }
                })
                .catch(error => console.error('Error:', error));
            });
        });
        
        // Function to update the subtotal after removing an item
        function updateSubtotal(subtotal) {
            var subtotalElements = document.querySelectorAll('.cart-subtotal .amount');
            subtotalElements.forEach(function(element) {
                element.textContent = '$' + subtotal;
            });
            
            var totalElements = document.querySelectorAll('.order-total .amount');
            totalElements.forEach(function(element) {
                element.textContent = '$' + subtotal;
            });
        }
    });
</script>

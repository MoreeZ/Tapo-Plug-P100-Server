document.addEventListener('DOMContentLoaded', function() {
    const triggerButton = document.getElementById('triggerButton');
    const buttonText = document.getElementById('buttonText');
    const loadingSpinner = document.getElementById('loadingSpinner');
    const responseMessage = document.getElementById('responseMessage');
    const statusText = document.getElementById('statusText');

    triggerButton.addEventListener('click', async function() {
        // Show loading state
        buttonText.textContent = 'Opening Door...';
        loadingSpinner.style.display = 'inline-block';
        triggerButton.disabled = true;
        
        try {
            const response = await fetch('http://localhost:8000/trigger', {
                method: 'GET',
            });
            
            // Display response
            responseMessage.style.display = 'block';
            
            if (response.ok) {
                const data = await response.text();
                statusText.textContent = `Door Status: ${data}`;
                statusText.className = 'success';
            } else {
                statusText.textContent = `Door Error: ${response.status} ${response.statusText}`;
                statusText.className = 'error';
            }
        } catch (error) {
            responseMessage.style.display = 'block';
            statusText.textContent = `Connection Error: ${error.message}`;
            statusText.className = 'error';
        } finally {
            // Reset button state
            buttonText.textContent = 'Open Vault Door';
            loadingSpinner.style.display = 'none';
            triggerButton.disabled = false;
        }
    });
});

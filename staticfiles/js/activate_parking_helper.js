document.addEventListener('DOMContentLoaded', function () {
    const helpIcons = document.querySelectorAll('.toggle-help'); // get all help icons

    helpIcons.forEach(function (icon) {
        
        icon.addEventListener('click', function () {
            // get associated help div ID
            const helpId = this.getAttribute('data-help-id'); 
            // retrive the relevant div by its id generated with forloop counter
            const helpDiv = document.getElementById(helpId); 
            
            // Toggle the display of the help div
            if (helpDiv.style.display === 'none' || helpDiv.style.display === '') {
                helpDiv.style.display = 'block'; // Show the div
            } else {
                helpDiv.style.display = 'none'; // Hide the div
            }
        });
    });
});
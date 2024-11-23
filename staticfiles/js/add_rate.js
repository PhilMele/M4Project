
document.addEventListener('DOMContentLoaded', function () {
    const helpLink = document.getElementById('toggle-help');
    const helpDiv = document.getElementById('help-parking-during-rate');

    helpLink.addEventListener('click', function (event) {
        event.preventDefault(); // Prevent default behavior of the <a> tag
        // Toggle the display of the help div
        if (helpDiv.style.display === 'none' || helpDiv.style.display === '') {
            helpDiv.style.display = 'block'; // Show the div
        } else {
            helpDiv.style.display = 'none'; // Hide the div
        }
    });
});

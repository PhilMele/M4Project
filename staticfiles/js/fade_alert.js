document.addEventListener('DOMContentLoaded', function () {
    // target alert messages
    const messages = document.querySelectorAll('.alert');
    messages.forEach((message) => {
        // remoove alert after 5 sec
        setTimeout(() => {
            message.classList.add('hide');
        }, 3000); 
        // remove element
        setTimeout(() => {
            message.remove(); 
        }, 3000);
    });
});
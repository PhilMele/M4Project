console.log("signup.js is active");


document.addEventListener('DOMContentLoaded', function() {
    
    // define form element
    const form = document.querySelector('form'); 

    // fields to validate
    const emailField = form.querySelector('input[name="email"]');
    const confirmEmailField= form.querySelector('input[name="email2"]')

    // email check credits: https://stackoverflow.com/questions/46155/how-can-i-validate-an-email-address-in-javascript
    emailField.addEventListener('input', () => {
        const email = emailField.value;
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        
        hideError(emailField);
        
        if (!emailPattern.test(email)) {
            displayError(emailField, "Email address is not valid.");
        }
    });

    // confirm email field
    confirmEmailField.addEventListener('input',()=>{
        const confirmEmail = confirmEmailField.value;

        hideError(confirmEmailField)

        if(confirmEmail !== emailField.value){
            displayError(confirmEmailField, "Email addresses do not match");
        }
    })

    const genError = (message) => {
        const error = document.createElement('div');
        error.className = 'error-message';
        error.style.color = 'red';
        error.textContent = message;
        return error;
    };

    function displayError(field, message) {
        let error = field.nextElementSibling;
        
        if (!error || !error.classList.contains('error-message')) {
            error = genError(message);
            field.insertAdjacentElement('afterend', error);
        } else {
            error.textContent = message;
        }
        
        field.classList.add('invalid');
    }

    function hideError(field) {
        const error = field.nextElementSibling;
        
        if (error && error.classList.contains('error-message')) {
            error.remove();
        }
        
        field.classList.remove('invalid');
    }

    // email confirmation
    // checkusername
    // password
    // password confirmation
});
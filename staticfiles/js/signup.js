document.addEventListener('DOMContentLoaded', function() {
    
    // define form element
    const form = document.querySelector('form'); 

    // fields to validate
    const emailField = form.querySelector('input[name="email"]');
    const confirmEmailField = form.querySelector('input[name="email2"]');
    const checkUsernamerField = form.querySelector('input[name="username"]');
    const checkPasswordField = form.querySelector('input[name="password1"]');
    const confirmPasswordField = form.querySelector('input[name="password2"]');

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
    confirmEmailField.addEventListener('input', () => {
        const confirmEmail = confirmEmailField.value;

        hideError(confirmEmailField);

        if (confirmEmail !== emailField.value) {
            displayError(confirmEmailField, "Email addresses do not match");
        }
    });

    // checks if username is within 4 to 150 characters
    checkUsernamerField.addEventListener('input', () => {
        const username = checkUsernamerField.value;
        const minChar = 4;
        const maxChar = 150;

        hideError(checkUsernamerField);

        if (username.length < minChar || username.length > maxChar) {
            displayError(checkUsernamerField, "Your username needs to be between 4 to 150 characters");
        }
    });

    // checks if password meets requirements:
    checkPasswordField.addEventListener('input', () => {
        const password = checkPasswordField.value; // Declare password variable here
        const minChar = 8;

        hideError(checkPasswordField);

        if (password.length < minChar) {
            displayError(checkPasswordField, "Your password must contain at least 8 characters.");
        }

        if (!/[0-9]/.test(password)) {
            displayError(checkPasswordField, "Password must contain at least one digit.");
        }

        if (!/[a-zA-Z!#$%&?]/.test(password)) {
            displayError(checkPasswordField, "Your password must contain at least one letter and one special character.");
        }
    });

    // Confirm password check
    confirmPasswordField.addEventListener('input', () => {
        const confirmPassword = confirmPasswordField.value;
        const password = checkPasswordField.value; // Use the password from checkPasswordField

        hideError(confirmPasswordField);

        if (confirmPassword !== password) {
            displayError(confirmPasswordField, "Your passwords do not match!");
        }
    });

    // Generate error message
    const genError = (message) => {
        const error = document.createElement('div');
        error.className = 'error-message';
        error.style.color = 'red';
        error.textContent = message;
        return error;
    };

    // Display error message
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

    // Hide error message
    function hideError(field) {
        const error = field.nextElementSibling;
        
        if (error && error.classList.contains('error-message')) {
            error.remove();
        }
        
        field.classList.remove('invalid');
    }

});

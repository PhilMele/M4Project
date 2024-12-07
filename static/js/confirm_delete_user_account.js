document.addEventListener('DOMContentLoaded', function () {

    const confirmDeleteBtn = document.getElementById('confirmDeleteBtn');
    const deleteAccountForm = document.querySelector('.delete-account-form');

    // Display options
    if (!confirmDeleteBtn) {
        console.error("Confirm Delete Button not found");
        return;
    }
    if (!deleteAccountForm) {
        console.error("Delete Account Form not found");
        return;
    }

    // addevent listner to confirm click
    confirmDeleteBtn.addEventListener('click', function () {

        deleteAccountForm.submit(); // submit form when clicked
    });
});

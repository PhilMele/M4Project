document.addEventListener('DOMContentLoaded', () => {
    const checkInButton = document.getElementById('provide-car-reg');
    const carRegModal = new bootstrap.Modal(document.getElementById('carRegBootstrapModal'));

    checkInButton.addEventListener('click', (e) => {
        carRegModal.show(); // display modal
    });
});
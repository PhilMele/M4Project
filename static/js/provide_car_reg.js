document.addEventListener('DOMContentLoaded', () => {
    const checkInButton = document.getElementById('provide-car-reg');
    const carRegModal = document.getElementById('carRegBootstrapModal');

    // if statemnt to prevent error showing in console
    // when elements dont exist when DOM is loaded
    if (checkInButton && carRegModal){
        const _carRegModal = new bootstrap.Modal(carRegModal);
        checkInButton.addEventListener('click', (e) => {
            _carRegModal.show(); // display modal
    });
    
    };
});
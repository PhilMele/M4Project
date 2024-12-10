document.addEventListener('DOMContentLoaded', function(){

  const latitudeField = document.getElementById("userLatitude");
  const longitudeField = document.getElementById("userLongitude");

  // Function to retrieve location
  function getLocation() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(showPosition);
    } else { 
      alert("Geolocation is not supported by this browser.");
    }
  }

  // Function to handle the position
  function showPosition(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;

    // Set values to the hidden inputs
    latitudeField.value = latitude;
    longitudeField.value = longitude;
  }

  // Trigger script only when fields are known
  if (latitudeField && longitudeField) {
    getLocation();
  }
});
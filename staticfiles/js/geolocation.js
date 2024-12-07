
document.addEventListener('DOMContentLoaded', function(){

  const latitudeField = document.getElementById("userLatitude")
  const longitudeField = document.getElementById("userLongitude")

  function getLocation() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(showPosition);
    } else { 
      alert("Geolocation is not supported by this browser.");
    }
  }

  function showPosition(position) {

    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;

    // adds value to hidden inputs in index.html
    latitudeField.value = latitude;
    longitudeField.value = longitude;

  }
  getLocation()
})
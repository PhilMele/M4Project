
document.addEventListener('DOMContentLoaded', function(){
  const x = document.getElementById("userLocation");

  const latitudeField = document.getElementById("userLatitude")
  const longitudeField = document.getElementById("userLongitude")

  function getLocation() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(showPosition);
    } else { 
      x.innerHTML = "Geolocation is not supported by this browser.";
    }
  }

  function showPosition(position) {

    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;

    // adds value to hidden inputs in index.html
    latitudeField.value = latitude;
    longitudeField.value = longitude;


    // TODO: REMOVE THIS BEFORE SUBMISSION
    x.innerHTML = "Latitude: " + position.coords.latitude + 
    "<br>Longitude: " + position.coords.longitude;
  }
  getLocation()
})
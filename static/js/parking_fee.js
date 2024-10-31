console.log("scripts.js is active for parking fee");

document.addEventListener('DOMContentLoaded', function(){

    // sets parking id as null by default
    let parkingId = "null";
    // captures parameter from url (if any)
    const path = window.location.pathname;
    const pathSplit = path.split('/');
    const parkingIdFromParam = pathSplit[pathSplit.length -2]
    console.log(`parking id is ${parkingIdFromParam}`);

    function fetchRates(){
        if (parkingIdFromParam == "null") {
            parkingId = "null";
        } else {
            parkingId = parkingIdFromParam;
        }

        console.log(`parking id = ${parkingId} `)
        
        if (parkingId){
            fetch(`/parking_activity/get_parking_rates/${parkingId}/`)
            .then(response => response.json())
            .then(data => {
                console.log("Fetched rates:", data);
             
        })
        }
    }
    
        // if there is a parameter change Parking ID
        // if user has selected a parking name 
    fetchRates()
  })
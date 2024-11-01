console.log("scripts.js is active for parking fee");

document.addEventListener('DOMContentLoaded', function(){

    // sets parking id as null by default
    let parkingId = "null";
    // captures parameter from url (if any)
    const path = window.location.pathname;
    const match = path.match(/\/enter\/(\d+)\//);
    const parkingIdFromParam = match ? match[1] : null;
    // sets parking id with either of value or null
    parkingId = parkingIdFromParam || "null";
    console.log(`parking id is ${parkingIdFromParam}`);
    
    // look for changes if the user has selected a parking manually
    const manuallySelectedParking = document.getElementById('parking-select');
    console.log("manuallySelectedParking=", manuallySelectedParking);

    if(manuallySelectedParking){
        manuallySelectedParking.addEventListener('change', function(){
            console.log("this is getting accessed")
            parkingId = this.value || "null";
            console.log(`Updated parking id is ${parkingId}`);
            // only trigger fetchRates() if parking_id is not null
            // to avoid 404 error in console
            if (parkingId !== "null"){
                fetchRates();
            }
            
        })

    }
    
    function fetchRates(){
        console.log(`ParkindId in fetchRates= ${parkingId}`);
        if(parkingId){
            fetch(`/parking_activity/get_parking_rates/${parkingId}/`)
            .then(response => response.json())
            .then(data =>{
                console.log("Fetched rates", data);
                renderRatesTable(data);
            })
            .catch(error => console.error("theres an error when getting the rates", error))
        }   
    }

    function renderRatesTable(data){

        // get the body of the table
        const tbody = document.querySelector("table tbody")
        tbody.innerHTML = "";

        // Adds data to table rwos
        data.forEach(rate=>{
            const tableRow = document.createElement('tr');
            tableRow.innerHTML = `
                <tb>${rate.rate_name}</tb>
                <tb>${rate.hour_range}</tb>
                <tb>${rate.rate}</tb>
            `;
            tbody.appendChild(tableRow);
        });
    }
    
    // only trigger fetchRates() if parking_id is not null
    // to avoid 404 error in console
    if (parkingId !== "null"){
        fetchRates()
    }
  })
console.log("scripts.js is active for parking fee");

document.addEventListener('DOMContentLoaded', function(){

    // sets parking id as null by default
    let parkingId = "null";
    // captures parameter from url (if any)
    const path = window.location.pathname;
    const pathSplit = path.split('/');
    const parkingIdFromParam = pathSplit[pathSplit.length -2]
    console.log(`parking id is ${parkingIdFromParam}`);

    // Collect rates from `get_parking_rates()`
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
                renderRatesTable(data);
        })
        .catch(error => console.error("theres an error when getting the rates", error))
        }
    }

    function renderRatesTable(data){

        // get the body of the table
        const tbody = document.querySelector("table tbody")
        tbody.inner = "";

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

    
        // if there is a parameter change Parking ID
        // if user has selected a parking name 
    fetchRates()
  })
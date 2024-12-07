document.addEventListener('DOMContentLoaded', function(){

    // sets parking id as null by default
    let parkingId = "null";
    // captures parameter from url (if any)
    const path = window.location.pathname;
    const match = path.match(/\/enter\/(\d+)\//);
    const parkingIdFromParam = match ? match[1] : null;
    // sets parking id with either of value or null
    parkingId = parkingIdFromParam || "null";
   
    
    // look for changes if the user has selected a parking manually
    const manuallySelectedParking = document.getElementById('parking-select');
   
    if(manuallySelectedParking){
        manuallySelectedParking.addEventListener('change', function(){
            
            parkingId = this.value || "null";
            
            // only trigger fetchRates() if parking_id is not null
            // to avoid 404 error in console
            if (parkingId !== "null"){
                fetchRates();
            }
            
        })

    }
    
    function fetchRates(){
       
        if(parkingId){
            fetch(`/parking_activity/get_parking_rates/${parkingId}/`)
            .then(response => response.json())
            .then(data =>{
                
                renderRatesTable(data);
            })
            .catch(error => console.error("theres an error when getting the rates", error))
        }   
    }

    function renderRatesTable(data){

        // get the body of the table
        const table = document.getElementById("ratesTable");
        const tbody = document.querySelector("table tbody")
        tbody.innerHTML = "";

        if(data.length>0){
            
            // shows table
            table.style.display ="table"
            // Adds data to table rwos

            data.forEach(rate=>{
                const tableRow = document.createElement('tr');
                tableRow.innerHTML = `
                <tr>
                    <td>${rate.rate_name}</td>
                    <td>${rate.hour_range}</td>
                    <td>£${rate.rate}</td>
                </tr>
                `;
                tbody.appendChild(tableRow);
            });
        }else{
            table.style.display = "none"
        }
    }
    
    // only trigger fetchRates() if parking_id is not null
    // to avoid 404 error in console
    if (parkingId !== "null"){
        fetchRates()
    }
  })
document.getElementById("payment-form").addEventListener("submit", (e) => {
    e.preventDefault();

    const recipient = document.getElementById("recipient_no").value;
    const network = document.getElementById("network").value;
    const dataPlan = document.getElementById("data_plan").value;
        
    const data = {
        'recipient' : recipient,
        'network'   : network,
        'plan'      : dataPlan
    }
    console.log(data);
    fetch("/buy_data/", {
        method: "POST",
        headers: {
            "Content-Type"     : "application/json",
            "Accept"           : "application/json, text/plain, */*",
            "Accept-language"  : "en-GB,en-US;q=0.9,en;q=0.8",
        },
        body: JSON.stringify(data), // Convert the data to a JSON string
    }).then(res => res.json())
    .then(res => {
        console.log(res)

        if (res.status == true){
            document.querySelector("#submit").classList.remove('active');
            document.querySelector(".message_success-col").classList.add('active');
            document.getElementById("message_success").innerHTML = res.message
        }
        else{
            document.querySelector(".message_error-col").classList.add('active');
            document.getElementById("message_error").innerHTML = res.message
        }
    })
    .catch(console.error);
});
const recipient = document.getElementById("recipient_no").value;
const network = document.getElementById("network").value;
const dataPlan = document.getElementById("data_plan").value;

document.getElementById("payment-form").addEventListener("submit", (e) => {
    e.preventDefault();
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const data = {
        'recipient' : recipient,
        'network'   : network,
        'plan'      : dataPlan
    }
    fetch("https://binx-crypto.onrender.com/buy_data/", {
        method: "POST",
        mode: "same-origin",
        credentials: "same-origin",
        headers: {
            "Content-Type"     : "application/json",
            "Accept"           : "application/json, text/plain, */*",
            "Accept-language"  : "en-GB,en-US;q=0.9,en;q=0.8",
            "X-CSRFToken"      : csrftoken,
        },
        body: JSON.stringify(data)
    }).then(res => res.json())
    .then(res => {
        if (res.status == true){
            document.querySelector("#submit").classList.remove('active');
            document.querySelector(".message_success-col").classList.add('active');
            document.getElementById("message_success").innerHTML = res.message
        }
        else if (res.status == false){
            document.querySelector(".message_error-col").classList.add('active');
            document.getElementById("message_error").innerHTML = res.message
        }
    })
    .catch(console.error);
});
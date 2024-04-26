const amountBox = document.querySelector("#amount_box");

function listBanks(){
    fetch("/banks/", {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            "Accept": "application/json, text/plain, */*",
            "Accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        },
    }).then(response => response.json()).then(banks => {
        // Get the select field
        const bankField = document.getElementById('bank');
        bankField.innerHTML = '<option value="0">Select Bank</option>';
        // Add options to the select field
        banks[2].forEach(bank => {
            let option = document.createElement('option');
            option.text = bank.name;
            option.value = bank.code;
            option.setAttribute('data-subtext', bank.name);
            bankField.appendChild(option);
        });
    }).catch (error => console.log(error));
}
listBanks();

document.getElementById("payment-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const recipientInput = document.querySelector("#recipient");
    const bankInput = document.querySelector("#bank");
    const submitButton = document.querySelector("#submit");
    const messageSuccessCol = document.querySelector(".message_success-col");
    const messageErrorCol = document.querySelector(".message_error-col");
    const messageSuccess = document.getElementById("message_success");
    const messageError = document.getElementById("message_error");

    const data = {
        'recipient': recipientInput.value,
        'bank': bankInput.value,
    };
    try {
        document.getElementById('loader').style.display="flex";
        document.getElementById("main").classList.add("d-none");
        const response = await fetch("/make_transfer/", {
            method: "POST",
            headers: {
                'Accept': 'application/json, text/plain, */*',
                'Content-Type': 'application/json', // Set the content type header
                'Accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            },
            body: JSON.stringify(data), // Convert the data to a JSON string
        });
        if (!response.ok) {
            document.getElementById('loader').style.display="none";
            document.getElementById("main").classList.remove("d-none");
            throw new Error('Network response was not ok');
        }
      
        const res = await response.json();
        if (res[0]) {
            // Correctly access the account_name and message properties
            submitButton.classList.remove('active');
            messageSuccessCol.classList.add('active');
            messageSuccess.innerHTML = res[1];
            document.querySelector("#transcx_id").innerHTML = res[2].transfer_id;
            document.querySelector("#recipient_name").value = res[2].account_name;
            document.querySelector("#submit").setAttribute("data-bs-toggle", "modal");
            document.querySelector("#submit").setAttribute("data-bs-target", "#modalId");
        } else {
            messageErrorCol.classList.add('active');
            // Ensure the error message is correctly accessed
            messageError.innerHTML = res[1] || 'An error occurred.';
        }
      
        document.getElementById('loader').style.display="none";
        document.getElementById("main").classList.remove("d-none");
    } catch (error) {
        document.getElementById('loader').style.display="none";
        document.getElementById("main").classList.remove("d-none");
        
        console.error('There was a problem with your fetch operation:', error);
    }    
});


const recipient_name = document.getElementById("recipient_name");
const accountInput = document.getElementById("recipient");
accountInput.addEventListener("keydown", (e) => {
    recipient_name.value = ""
    document.querySelector(".message_success-col").classList.remove('active');
    document.querySelector(".message_error-col").classList.remove('active');
    if (e.key === "Enter") {
        e.preventDefault();
        document.querySelector("#submit").click();
    }
})


function Transfer() {
    document.querySelector(".message_success-col").classList.remove('active');
    document.querySelector(".message_error-col").classList.remove('active');
}


const completeTrans = document.querySelector("#completeTransfer");
function Transact(){
    const recipientInput = document.querySelector("#recipient");
    const bankInput = document.querySelector("#bank");
    const amountInput = document.querySelector("#amount");
    const transactionPin = document.querySelector("#transactionPin");

    const data = {
        'transfer_id': document.querySelector("#transcx_id").innerHTML,
        'pin': transactionPin.value
    };

    fetch("/complete_transfer/", {
        method: "POST",
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json', // Set the content type header
            'Accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        },
        body: JSON.stringify(data), // Convert the data to a JSON string
    })
    .then(response => response.json())
    .then(res => {
        if (res.status == true){
            window.location.href = "/transfer/"+data.transfer_id+"/";
        }
        else if (res.status == false){
            document.querySelector(".message_error-col").classList.add('active');
            document.getElementById("message_error").innerHTML = res.message
        }
    })
    .catch(error => console.error('There was a problem with your fetch operation:', error));
}

completeTrans.addEventListener("submit", (e) => {
    e.preventDefault();
    Transact();
});
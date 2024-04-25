fetch("https://api.paystack.co/bank?currency=NGN&transferRecipient=false&country=Nigeria", {
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
      banks['data'].forEach(bank => {
        let option = document.createElement('option');
        option.text = bank.name;
        option.value = bank.code;
        option.setAttribute('data-subtext', bank.name);
        bankField.appendChild(option);
      });
  })
  .catch(console.error);
  
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

  document.getElementById("payment-form").addEventListener("submit", (e) => {

      e.preventDefault();
      const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
      const data = {
          'recipient' : document.querySelector("#recipient").value,
          'bank'     : document.querySelector("#bank").value,
          'token'     : document.querySelector("#token").value
      }
      fetch("https://api.paystack.co/bank/resolve?account_number="+data.recipient+"&bank_code="+data.bank+"&currency=NGN", {
          method: "GET",
          headers: {
            'Content-Type'     : 'application/json',
            'Accept'           : 'application/json, text/plain, */*',
            'Accept-language'  : 'en-GB,en-US;q=0.9,en;q=0.8',
            'Authorization'    : 'Bearer '+data.token,
          }
      }).then(res => res.json())
      .then(res => {
          if (res.status == true){
              recipient_name.value = res.data.account_name;
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
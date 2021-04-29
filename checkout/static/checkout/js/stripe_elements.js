var stripe_public_key = $('#id_stripe_public_key').text().slice(1,-1);
var client_secret = $('#id_client_secret').text().slice(1,-1);
var stripe = Stripe(stripe_public_key);

var elements = stripe.elements();
var style = {
    base: {
      color: "#60547c",
      fontFamily: 'Roboto, sans-serif',
      fontSmoothing: "antialiased",
      fontSize: "16px",
      "::placeholder": {
        color: "#60547c"
      }
    },
    invalid: {
      fontFamily: 'Roboto, sans-serif',
      color: "#ff4056",
      iconColor: "#ff4056"
    }
  };


var card = elements.create("card", { style: style });
    // Stripe injects an iframe into the DOM
card.mount("#card-element");

/* card.on("change", function (event) {
    // Disable the Pay button if there are no card details in the Element
    document.querySelector("button").disabled = event.empty;
    document.querySelector("#card-error").textContent = event.error ? event.error.message : "";
  }); */


    
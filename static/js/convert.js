// Callback for converting arabic to numeric characters.
to_arabic = () => {
    event.preventDefault();
    let user_input = document.querySelector('#arabic_input').value;
    let result = document.querySelector('#arabic_results');
    fetch(`/to_roman/${user_input}`, {method : 'POST'})
    .then(data => data.json())
    .then(data => {
        let result = document.querySelector('#arabic_results');
        result.value = data.result;
    })
    .catch(error => result.value = '???');
}

// Callback for converting numeric to roman characters.
to_roman = () => {
    event.preventDefault();
    let user_input = document.querySelector('#roman_input').value;
    let result = document.querySelector('#roman_result');
    fetch(`/to_arabic/${user_input}`, {method : 'POST'})
    .then(data => data.json())
    .then(data => {
        result.value = data.result;
    })
    .catch(error => result.value = '???');
}

// Attaching event listeners here:
let arabic_button = document.querySelector('#roman_to_arab');
let roman_button = document.querySelector('#arab_to_roman');

arabic_button.addEventListener('click', to_roman);
roman_button.addEventListener('click', to_arabic);
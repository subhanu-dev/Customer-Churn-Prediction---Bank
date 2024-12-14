
const form = document.getElementById('churnForm');

function validateForm(event) {
    event.preventDefault(); // Prevent default form submission
    let isValid = true;
    const messages = [];

    // Access fields
    const creditScore = document.getElementById('credit_score');
    const age = document.getElementById('age');
    const tenure = document.getElementById('tenure');
    const balance = document.getElementById('balance');
    const productsNumber = document.getElementById('products_number');
    const estimatedSalary = document.getElementById('estimated_salary');


    // Validation Rules
    if (creditScore.value < 300 || creditScore.value > 850) {
        isValid = false;
        messages.push("Credit Score must be between 300 and 850.");
    }

    if (age.value < 18 || age.value > 100) {
        isValid = false;
        messages.push("Age must be between 18 and 100.");
    }

    if (tenure.value < 0 || tenure.value > 20) {
        isValid = false;
        messages.push("Invalid input for Tenure.");
    }

    if (balance.value < 0) {
        isValid = false;
        messages.push("Balance cannot be negative.");
    }

    if (productsNumber.value < 1 || productsNumber.value > 5) {
        isValid = false;
        messages.push("Number of Products must be between 1 and 5.");
    }

    if (estimatedSalary.value < 0) {
        isValid = false;
        messages.push("Estimated Salary cannot be negative.");
    }

    // Display Error Messages
    const errorContainer = document.getElementById('errorMessages');
    errorContainer.innerHTML = ""; // Clear previous messages
    if (!isValid) {
        messages.forEach((msg) => {
            const error = document.createElement('p');
            error.textContent = msg;
            error.style.color = "red";
            errorContainer.appendChild(error);
        });
    } else {
        // Proceed with form submission if valid
        submitForm();
    }
}

// Bind validation to button click
form.addEventListener('submit', validateForm);



async function submitForm() {
    // Collect form data
    const form = document.getElementById('churnForm');
    const formData = new FormData(form);

    // Transform form data into JSON
    const country = formData.get('country'); // Get the selected country
    const balance = formData.get('balance')
    const data = {
        credit_score: parseInt(formData.get('credit_score')),
        age: parseInt(formData.get('age')),
        tenure: parseInt(formData.get('tenure')),
        balance: parseFloat(formData.get('balance')),
        products_number: parseInt(formData.get('products_number')),
        credit_card: parseInt(formData.get('credit_card')),
        active_member: parseInt(formData.get('active_member')),
        estimated_salary: parseFloat(formData.get('estimated_salary')),
        zero_balance: balance === 0 ? 1 : 0,
        country_Germany: country === 'Germany' ? 1 : 0, // Germany encoded as 1
        country_Spain: country === 'Spain' ? 1 : 0,    // Spain encoded as 1
        // France is automatically handled as Germany = 0 and Spain = 0
        gender_Male: formData.get('gender') === 'Male' ? 1 : 0 // Gender encoding
    };

    try {
        // Sending data to the API
        const response = await fetch('http://127.0.0.1:8000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        // Process the response
        if (response.ok) {
            const result = await response.json();
            alert(`Prediction: ${result.prediction}\nProbability:\n - Churn: ${result.probability.churn}\n - Not Churn: ${result.probability.not_churn}`);
        } else {
            alert('An error occurred while processing the prediction.');
        }

    } catch (error) {
        console.error('Error:', error);
        alert('Failed to connect to the prediction API.');
    }
}
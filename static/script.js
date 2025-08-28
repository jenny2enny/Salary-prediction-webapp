document.getElementById('salaryForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const age = document.getElementById('age').value;
    const education = document.getElementById('education').value;
    const experience = document.getElementById('experience').value;

    // Prepare data for backend
    const data = {
        age: Number(age),
        education: education,
        experience: Number(experience)
    };

    // Send request to backend (update URL as needed)
    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        const result = await response.json();
        document.getElementById('result').textContent =
            result.salary ? `Predicted Salary: $${result.salary}` : 'Prediction failed.';
    } catch (error) {
        document.getElementById('result').textContent = 'Error: Could not get prediction.';
    }
});

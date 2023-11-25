// main.js
async function processText() {
    const text = document.getElementById("textInput").value;
    const options = Array.from(document.querySelectorAll('input[name="options"]:checked'))
        .map(checkbox => checkbox.value);

    const data = { text, options };

    const response = await fetch('http://localhost:8000/api/process_text', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });

    const result = await response.json();
    document.getElementById("result").innerText = `Result: ${result.result}`;
}
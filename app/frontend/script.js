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

    // document.getElementById("result").innerText = `${result.result}`;

    // Открытие нового окна и вставка результата
    const resultWindow = window.open('', '_blank');
    resultWindow.document.write(`
        <html>
            <head>
                <title>Result</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        padding: 20px;
                        white-space: pre-wrap; /* Сохраняем переносы строк */
                    }
                </style>
            </head>
            <body>${result.result}</body>
        </html>
    `);
    resultWindow.document.close();
}
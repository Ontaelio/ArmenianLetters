// main.js

document.addEventListener('DOMContentLoaded', function () {
    // В этом блоке кода обрабатывается событие загрузки страницы
    const fileInput = document.getElementById('fileInput');
    const fileTextElement = document.getElementById('fileText');

    // Обновление текста с именем файла при изменении файла
    fileInput.addEventListener('change', function () {
        const file = fileInput.files[0];

        // Получение типа файла
        const fileType = file.type;

        // Получение размера файла в КБ
        const fileSizeKB = file.size / 1024;

        // Проверка типа файла (исключительно текстовый файл)
        if (!fileType.startsWith('text/')) {
            alert('Некорректный тип файла. Пожалуйста, выберите текстовый файл.');
            return;
        }

        // Проверка размера файла (не больше 500 КБ)
        if (fileSizeKB > 800) {
            alert('Размер файла превышает 800 КБ. Пожалуйста, выберите файл размером до 500 КБ.');
            return;
        }

        fileTextElement.innerText = file ? `Выбран файл: ${file.name}` : '';
        // document.getElementById('optionsForm').submit();
    });
});


async function processFile() {
    // Получение содержимого файла, если выбран
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];


    // Обновление текста с именем файла
    // fileInput.addEventListener('change', function () {
    //     const file = fileInput.files[0];
    //     fileTextElement.innerText = file ? `Selected File: ${file.name}` : '';
    // });

    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            // Замена текста на содержимое файла
            document.getElementById('textInput').value = e.target.result;
        };
        reader.readAsText(file);
    }
}


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
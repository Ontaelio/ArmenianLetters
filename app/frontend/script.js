// main.js

document.addEventListener('DOMContentLoaded', function () {
    // В этом блоке кода обрабатывается событие загрузки страницы
    const fileInput = document.getElementById('fileInput');
    const fileTextElement = document.getElementById('fileText');

    // Разрешенные MIME-типы
    const allowedMimeTypes = ['text/plain', 'application/epub+zip'];

    // Обновление текста с именем файла при изменении файла
    fileInput.addEventListener('change', function () {
        const file = fileInput.files[0];

        // Получение типа файла
        const fileType = file.type;

        // Получение размера файла в КБ
        const fileSizeKB = file.size / 1024;

        // Проверка типа файла (разрешенные MIME-типы)
        if (!allowedMimeTypes.includes(fileType)) {
            showError('Недопустимый тип файла. Пожалуйста, выберите файл TXT или EPUB.');
            return;
        }

        // Проверка размера файла (не больше 500 КБ)
        if (fileSizeKB > 800) {
            alert('Размер файла превышает 800 КБ. Пожалуйста, выберите файл меньше размером.');
            return;
        }

        fileTextElement.innerText = file ? `Выбран файл: ${file.name}` : '';
        // document.getElementById('optionsForm').submit();
    });
});


async function processAndDownload() {
    // Получение содержимого файла, если выбран
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    const options = Array.from(document.querySelectorAll('input[name="options"]:checked'))
        .map(checkbox => checkbox.value);

    if (file) {
        const fileType = file.type;
        const formData = new FormData();
        formData.append('file', file);
        formData.append('options', JSON.stringify(options));

        if (fileType === 'text/plain') {

            fetch('/api/process_file', {
                method: 'POST',
                body: formData
            })
                .then(response => response.blob())
                .then(blob => {
                    // Создайте новый файл из полученного blob
                    const newFile = new File([blob], 'processed_file.txt', {type: 'text/plain'});

                    // Скачайте новый файл
                    const a = document.createElement('a');
                    const url = URL.createObjectURL(newFile);
                    a.href = url;
                    a.download = 'processed_file.txt';
                    document.body.appendChild(a);
                    a.click();
                    window.URL.revokeObjectURL(url);
                    document.body.removeChild(a);
                })
                .catch(error => {
                    console.error('Error processing file:', error);
                });
        } else if (fileType === 'application/epub+zip') {

            fetch('/api/process_file', {
                method: 'POST',
                body: formData
            })
                .then(response => response.blob())
                .then(blob => {
                    // Создайте новый файл из полученного blob
                    const newFile = new File([blob], 'processed_book.epub', {type: 'application/epub+zip'});

                    // Скачайте новый файл
                    const a = document.createElement('a');
                    const url = URL.createObjectURL(newFile);
                    a.href = url;
                    a.download = 'processed_book.epub';
                    document.body.appendChild(a);
                    a.click();
                    window.URL.revokeObjectURL(url);
                    document.body.removeChild(a);
                })
                .catch(error => {
                    console.error('Error processing file:', error);
                });
        }
    }
}

async function processFile() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    const reader = new FileReader();

    if (file) {
        const fileType = file.type;

        if (fileType === 'text/plain') {
            reader.onload = function (e) {
                // Замена текста на содержимое файла
                document.getElementById('textInput').value = e.target.result;
            };
        reader.readAsText(file);
        }

        else if (fileType === 'application/epub+zip') {
            document.getElementById('textInput').value = 'Привет как дила?'
        }
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
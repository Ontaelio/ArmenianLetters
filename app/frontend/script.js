// main.js

document.addEventListener('DOMContentLoaded', function () {
    // В этом блоке кода обрабатывается событие загрузки страницы
    const fileInput = document.getElementById('fileInput');
    const fileTextElement = document.getElementById('fileText');
    const allowedMimeTypes = ['text/plain', 'application/epub+zip'];

    fileInput.addEventListener('change', function () {
        const file = fileInput.files[0];
        const fileType = file.type;
        const fileSizeKB = file.size / 1024;
        const sizeByType = {
            'text/plain': 810,
            'application/epub+zip': 2100
        }
        if (!allowedMimeTypes.includes(fileType)) {
            alert('Недопустимый тип файла. Пожалуйста, выберите файл TXT или EPUB.');
            return;
        }

        if (fileSizeKB > sizeByType[fileType]) {
            alert('Размер файла превышает 800 КБ (txt) / 2 МБ (epub). Пожалуйста, выберите файл меньше размером.');
            return;
        }

        fileTextElement.innerText = file ? `Выбран файл: ${file.name}` : '';
    });
});


async function processAndDownload() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    const options = Array.from(document.querySelectorAll('input[name="options"]:checked'))
        .map(checkbox => checkbox.value);
    const allowedMimeTypes = ['text/plain', 'application/epub+zip'];

    if (file) {
        const fileType = file.type;
        const formData = new FormData();
        const fileName = file.name;
        const modifiedFileName = fileName.replace(/(\.[\w\d]+)$/, "-ARM$1");
        formData.append('file', file);
        formData.append('options', JSON.stringify(options));

        if (allowedMimeTypes.includes(fileType)) {

            const processingMessage = document.getElementById('processingMessage');
            processingMessage.style.display = 'block';

            fetch('/api/process_file', {
                method: 'POST',
                body: formData
            })
                .then(response => response.blob())
                .then(blob => {
                    const newFile = new File([blob], modifiedFileName, {type: fileType});

                    const a = document.createElement('a');
                    const url = URL.createObjectURL(newFile);
                    a.href = url;
                    a.download = modifiedFileName;
                    document.body.appendChild(a);
                    a.click();
                    window.URL.revokeObjectURL(url);
                    document.body.removeChild(a);

                })
                .then(() => {
                processingMessage.style.display = 'none';})
                .catch(error => {
                    console.error('Error processing file:', error);
                    alert('Ошибка обработки файла')})

        } else alert('Что-то пошло не так с типом файла')
    }

    else alert('Выберите файл');
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
            const formData = new FormData();
            formData.append('file', file);

            fetch('/api/get_text_from_epub', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                //console.log('Response from server:', data);
                document.getElementById('textInput').value = data.result
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error uploading file');
            });

        }
    }

    else alert('Выберите файл')

}



async function processText() {

    const text = document.getElementById("textInput").value;
    const options = Array.from(document.querySelectorAll('input[name="options"]:checked'))
        .map(checkbox => checkbox.value);

    const data = { text, options };

    const response = await fetch('/api/process_text', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });

    const result = await response.json();

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

document.addEventListener("DOMContentLoaded", function () {
    document.addEventListener("click", function (event) {
        const target = event.target;

        if (target.classList.contains("topic-title")) {
            const topic = target.closest('.topic');

            if (topic) {
                topic.classList.toggle("active");
            }
        }
    });
});

function updateButtonsVisibility() {
    const fileInput = document.getElementById("fileInput");
    const uploadButton = document.getElementById("uploadButton");
    const downloadButton = document.getElementById("downloadButton");
    // const alredy_selected = document.getElementById('fileText').innerText;

    if (fileInput.files.length > 0){
        // Файл выбран, показываем кнопки
        uploadButton.style.display = "inline-block";
        downloadButton.style.display = "inline-block";
    } else {
        // Файл не выбран, скрываем кнопки
        uploadButton.style.display = "none";
        downloadButton.style.display = "none";
    }
}
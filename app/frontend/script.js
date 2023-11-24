// frontend/script.js
document.getElementById('getDataButton').addEventListener('click', getData);

async function getData() {
    try {
        const response = await fetch('http://localhost:8000/api/v1/some_endpoint');
        if (!response.ok) {
            throw new Error('Failed to fetch data from API');
        }
        const data = await response.json();
        document.getElementById('dataContainer').textContent = JSON.stringify(data, null, 2);
    } catch (error) {
        console.error(error);
        document.getElementById('dataContainer').textContent = 'Error fetching data from API';
    }
}
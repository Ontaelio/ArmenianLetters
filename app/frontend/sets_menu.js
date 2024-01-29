// // frontend/sets_menu.js
// document.addEventListener("DOMContentLoaded", async () => {
//     const topicsContainer = document.getElementById("topicsContainer");
//
//     try {
//         const response = await fetch('http://localhost:8000/api/sets');
//         const setsData = await response.json();
//
//         // Создаем элементы для каждой темы
//         for (const setName in setsData) {
//             const fullSet = setsData[setName];
//
//             const topicDiv = document.createElement("div");
//             topicDiv.classList.add("topic");
//
//             const titleDiv = document.createElement("div");
//             titleDiv.classList.add("topic-title");
//             titleDiv.innerText = setName;
//
//             const contentDiv = document.createElement("div");
//             contentDiv.classList.add("content");
//
//             for (const columnData in fullSet) {
//                 const columnDiv = document.createElement("div");
//                 columnDiv.classList.add("column")
//
//                 columnData.values.forEach(value => {
//                     const checkboxLabel = document.createElement("label");
//                     checkboxLabel.title = value.title;
//                     const checkboxInput = document.createElement("input");
//
//                     checkboxInput.type = "checkbox";
//                     checkboxInput.name = "options";
//                     checkboxInput.value = value.front_name;
//
//                     checkboxLabel.appendChild(checkboxInput);
//                     checkboxLabel.appendChild(document.createTextNode(` ${value.name}`));
//
//                     columnDiv.appendChild(checkboxLabel);
//                 })
//
//                 contentDiv.appendChild(columnDiv)
//             }
//
//             topicDiv.appendChild(titleDiv);
//             topicDiv.appendChild(contentDiv);
//
//             topicsContainer.appendChild(topicDiv);
//
//             // // Создаем чекбоксы
//             // topic.values.forEach(value => {
//             //     const checkboxLabel = document.createElement("label");
//             //     const checkboxInput = document.createElement("input");
//             //
//             //     checkboxInput.type = "checkbox";
//             //     checkboxInput.name = "options";
//             //     checkboxInput.value = value;
//             //
//             //     checkboxLabel.appendChild(checkboxInput);
//             //     checkboxLabel.appendChild(document.createTextNode(` ${value}`));
//             //
//             //     contentDiv.appendChild(checkboxLabel);
//             // });
//             //
//             // topicDiv.appendChild(titleDiv);
//             // topicDiv.appendChild(contentDiv);
//             //
//             // topicsContainer.appendChild(topicDiv);
//         }
//     } catch (error) {
//         console.error("Error fetching topics:", error);
//     }
// });

document.addEventListener("DOMContentLoaded", async () => {
    const topicsContainer = document.getElementById("topicsContainer");

    try {
        const response = await fetch('http://localhost:8000/api/sets_front');
        const setsData = await response.json();

        // Создаем элементы для каждой темы
        for (const setName in setsData) {
            const fullSet = setsData[setName];

            const topicDiv = document.createElement("div");
            topicDiv.classList.add("topic");

            const titleDiv = document.createElement("div");
            titleDiv.classList.add("topic-title");
            titleDiv.innerText = setName;

            const contentDiv = document.createElement("div");
            contentDiv.classList.add("content");

            for (const columnNum in fullSet) {
                const columnData = fullSet[columnNum]

                const columnDiv = document.createElement("div");
                columnDiv.classList.add("column");

                for (const value of columnData) {
                    const checkboxLabel = document.createElement("label");
                    checkboxLabel.title = value.title;
                    const checkboxInput = document.createElement("input");

                    checkboxInput.type = "checkbox";
                    checkboxInput.name = "options";
                    checkboxInput.value = value.front_name;

                    if (value.offset) {
                        checkboxLabel.appendChild(document.createTextNode("\u00A0\u00A0\u00A0"))
                    }
                    checkboxLabel.appendChild(checkboxInput);
                    checkboxLabel.appendChild(document.createTextNode(` ${value.name}`));

                    columnDiv.appendChild(checkboxLabel);
                }

                contentDiv.appendChild(columnDiv);
            }

            topicDiv.appendChild(titleDiv);
            topicDiv.appendChild(contentDiv);

            topicsContainer.appendChild(topicDiv);
        }
    } catch (error) {
        console.error("Error fetching sets:", error);
    }
});


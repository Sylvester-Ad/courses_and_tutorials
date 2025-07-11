const DEFAULT_DATE = "2025-12-22";

document.addEventListener("DOMContentLoaded", () => {

    // Define objects to store tasks
    const myTasks = {
        task1: [],
        task2: [],
        task3: []
    };

    function renderTasks(taskName, todoList) {
        todoList.innerHTML = "";
        myTasks[taskName].forEach(taskValue => {
            const taskItem = document.createElement("div");
            taskItem.innerHTML = `
                <div>${taskValue.name}</div>
                <div>${taskValue.date}</div>
                <button class="delete-btn js-delete-btn">Delete</button>
            `;
            // Add class for styling    
            taskItem.classList.add("todo-grid");

            // Add event listener for delete button
            const deleteBtn = taskItem.querySelector(".js-delete-btn");
            deleteBtn.addEventListener("click", function () {
                handleDeleteTask(taskName, taskValue);
                renderTasks(taskName, todoList);
            });
            todoList.appendChild(taskItem);
        });
    }

    function handleDeleteTask(taskName, taskValue) {
        const taskIndex = myTasks[taskName].findIndex(
            task => task.name === taskValue.name && task.date === taskValue.date
        );
        if (taskIndex > -1) {
            myTasks[taskName].splice(taskIndex, 1);
        }
    }

    const groups = document.querySelectorAll(".js-practice");

    groups.forEach(group => {
        const taskName = group.dataset.task;
        const inputEl = group.querySelector(".js-task-input");
        const button = group.querySelector(".js-add-btn");
        const todoList = group.querySelector(".js-tasks-list");


        button.addEventListener("click", () => {
            const name = inputEl.value.trim();
            const dateEl = group.querySelector(".js-input-date");
            const date = dateEl.value || DEFAULT_DATE;

            const taskValue = {
                name,
                date
            };


            if (name !== "") {
                // Check if the task already exists
                const taskExists = myTasks[taskName].some(task => task.name === name && task.date === date);
                if (taskExists) {
                    alert("Task already exists!");
                    return;
                }

                // Add task to the myTasks object
                myTasks[taskName].push(taskValue);
                // Render tasks
                renderTasks(taskName, todoList);
                // Clear input
                inputEl.value = "";
            }
                console.log(myTasks);
            }
        );

    });

})
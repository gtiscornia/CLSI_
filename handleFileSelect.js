function handleFileSelect(event) {
    const file = event.target.files[0];

    if (!file) {
        return;
    }

    const reader = new FileReader();
    reader.onload = function (e) {
        const content = e.target.result;
        const lines = content.split('\n');

        const taskList = document.getElementById('task-list');
        taskList.innerHTML = ''; // Clear previous tasks

        lines.forEach(line => {
            const [task, details] = line.split(',');
            const taskItem = document.createElement('li');
            taskItem.textContent = `${task} - ${details}`;
            taskList.appendChild(taskItem);
        });
    };

    reader.readAsText(file);
}

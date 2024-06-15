const tasks = document.querySelectorAll('.task');
const todoTasks = document.getElementById('todo-tasks');
const doneTasks = document.getElementById('done-tasks');

tasks.forEach(task => {
    task.addEventListener('dragstart', dragStart);
    task.addEventListener('dragend', dragEnd);
});

todoTasks.addEventListener('dragover', dragOver);
todoTasks.addEventListener('dragenter', dragEnter);
todoTasks.addEventListener('dragleave', dragLeave);
todoTasks.addEventListener('drop', dragDrop);

doneTasks.addEventListener('dragover', dragOver);
doneTasks.addEventListener('dragenter', dragEnter);
doneTasks.addEventListener('dragleave', dragLeave);
doneTasks.addEventListener('drop', dragDrop);

function dragStart() {
    this.classList.add('dragging');
}

function dragEnd() {
    this.classList.remove('dragging');
}

function dragOver(e) {
    e.preventDefault();
}

function dragEnter(e) {
    e.preventDefault();
    this.classList.add('over');
}

function dragLeave() {
    this.classList.remove('over');
}

function dragDrop() {
    const draggingTask = document.querySelector('.dragging');
    this.appendChild(draggingTask);
    draggingTask.classList.remove('dragging');
    this.classList.remove('over');
}

function dragDrop() {
    const draggingTask = document.querySelector('.dragging');
    this.appendChild(draggingTask);
    draggingTask.classList.remove('dragging');
    this.classList.remove('over');

    if (this.id === 'done-tasks') {
        draggingTask.style.display = 'none'; // Hide the task when dropped in completed tasks
    }
}
async function addTask() {
  await fetch("/tasks?title=Study&priority=2&due_date=2026-01-20", {
    method: "POST"
  });
  loadTasks();
}

async function loadTasks() {
  const res = await fetch("/tasks");
  const tasks = await res.json();
  document.getElementById("tasks").innerHTML =
    tasks.map(t => `<li>${t.title}</li>`).join("");
}

loadTasks();

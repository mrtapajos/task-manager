const form = document.getElementById("task-form");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  let taskName = document.getElementById("task-name").value;
  let taskDeadline = document.getElementById("task-deadline").value;
  let taskImportance = document.getElementById("task-importance").value;

  let taskPayload = {
    name: taskName,
    deadline: taskDeadline,
    importance: Number(taskImportance),
  };

  const response = await fetch("/tasks", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(taskPayload),
  });
  if (response.status == 200) {
    alert((await response.json()).message);
  } else {
    alert((await response.json()).message);
  }

  location.reload();
});


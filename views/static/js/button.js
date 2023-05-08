const deleteForm = document.getElementById("delete-form");

deleteForm.addEventListener("submit", async (event) => {
    const taskName = document.getElementById('task-name').value
    const response = await fetch(`/tasks/delete/${taskName}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({name: taskName}),
  });

  if (response.status == 200) {
    alert((await response.json()).message);
  } else {
    alert((await response.json()).message);
  }
  location.reload();
});

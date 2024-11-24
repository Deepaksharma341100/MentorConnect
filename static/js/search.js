function searchUser(event) {
  event.preventDefault();
  const idname = document.getElementById("idname").value.trim();
  console.log(idname);

  // Validate the idname is not empty
  if (idname) {
    window.location.href = `/user/${idname}`; // Redirect to the user's profile page
  } else {
    alert("Please enter a valid User ID.");
  }
}

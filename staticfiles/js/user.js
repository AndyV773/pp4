// delete user
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteModelConfirm = document.getElementById("delete-model-confirm");
// div element in edit profile for image
const div = document.getElementsByClassName('input-group')[0];


// removes the div element that contains the class name input-group
if (div) {
    div.remove();
}


/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated user ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific user.
*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let userId = e.target.getAttribute("data-user_id");
        deleteModelConfirm.href = `delete_user/${userId}/`;
    });
}

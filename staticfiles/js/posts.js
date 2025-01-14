const editModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const editButtons = document.getElementsByClassName("btn-edit");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");


/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Fetches the content of the corresponding comment.
* - Populates the `commentText` input/textarea with the comment's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
*/
for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let postId = e.target.getAttribute("data-post_id");
        let postContent = document.getElementById(`post${postId}`).innerText;

        let postText = document.getElementById(`id_content${postId}`);
        postText.value = postContent;

        const submitButton = document.getElementById(`submitButton${postId}`);
        submitButton.innerText = "Update";

        let postForm = document.getElementById(`postForm${postId}`);
        postForm.setAttribute("action", `edit_post/${postId}`);
    });
}

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let postId = e.target.getAttribute("data-post_id");
        deleteConfirm.href = `delete_post/${postId}`;
        deleteModal.show();
    });
}

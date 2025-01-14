const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("comment-form");
const submitButton = document.getElementById("submit-button");

const deleteModal = new bootstrap.Modal(document.getElementById("delete-modal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("delete-model-confirm");

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
        let commentId = e.target.getAttribute("data-comment_id");
        let commentContent = document.getElementById(`comment${commentId}`).innerText;
        commentText.value = commentContent;
        submitButton.innerText = "Update";
        commentForm.setAttribute("action", `edit_comment/${commentId}`);
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
        let commentId = e.target.getAttribute("data-comment_id");
        let postId = e.target.getAttribute("data-post_id");
        deleteConfirm.href = `${postId}/delete_comment/${commentId}`;
        deleteModal.show();
    });
}
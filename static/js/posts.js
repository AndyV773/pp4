const thePostButton = document.getElementById("the-post-button");
const theModelBody = document.getElementById("the-model-body");
const theModelLabel = document.getElementById("the-modal-label");

const editButtons = document.getElementsByClassName("btn-edit");
const postText = document.getElementById("id_content");
const postForm = document.getElementById("post-orm");
const submitButton = document.getElementById("submit-button");

const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteModelConfirm = document.getElementById("delete-model-confirm");
const deleteModal = new bootstrap.Modal(document.getElementById("delete-modal"));

// thePostButton.addEventListener("click", (e) => {
//     theModal.show();
// });

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
        console.log(postId);

        let postContent = document.getElementById(`post${postId}`).innerText;
        console.log(postContent);

        postText.id = `id_content${postId}`;
        postText.value = postContent;

        submitButton.innerText = "Update";
        postForm.setAttribute("action", `edit_post/${postId}`);
        // theModelConfirm.href = `edit_post/${postId}`;
        const postModal = new bootstrap.Modal(document.getElementById("post-modal"));
        postModal.show();
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
        console.log(postId);
        
        deleteModelConfirm.href = `delete_post/${postId}`;
        deleteModal.show();
    });
}

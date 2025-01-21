const thePostButton = document.getElementById("the-post-button");
const editButtons = document.getElementsByClassName("btn-edit");
const postText = document.getElementById("id_content");
const postForm = document.getElementById("post-form");
const submitButton = document.getElementById("post-submit-button");
const editPostTitle = document.getElementById("edit-post-title");
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteModelConfirm = document.getElementById("delete-model-confirm");


/**
 * Resets the post modal elements and form
 * for posting a new post
 */
if (thePostButton) {
    thePostButton.addEventListener("click", (e) => {
        editPostTitle.innerHTML = "";
        postText.value = "";
        postForm.setAttribute("action", "");
        submitButton.innerText = "Submit";
    });
}


/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated post's ID upon click.
* - Fetches the content of the corresponding comment.
* - Populates the `postText` input/textarea with the post's content for editing.
* - Updates the title to include "Edit"
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_post/{postId}` endpoint.
*/
for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let postId = e.target.getAttribute("data-post_id");
        let postContent = document.getElementById(`post${postId}`).innerText;
        editPostTitle.innerHTML = "Edit";
        postText.value = postContent;
        submitButton.innerText = "Update";
        postForm.setAttribute("action", `edit_post/${postId}/`);
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
        deleteModelConfirm.href = `delete_post/${postId}/`;
    });
}

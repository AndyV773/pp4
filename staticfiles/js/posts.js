const editButtons = document.getElementsByClassName("btn-edit");
const postText = document.getElementById("id_content");
const postForm = document.getElementById("postForm");
const submitButton = document.getElementById("submitButton");


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
        postText.value = postContent;
        submitButton.innerText = "Update";
        postForm.setAttribute("action", `edit_post/${postId}`);
    });
}

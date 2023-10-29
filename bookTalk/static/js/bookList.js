async function getReviews(book_id) {
    const reviewURL = "get-review-json/";
    return fetch(reviewURL).then((res) => res.json())
}

async function loadReviews(book_id) {
    let cardHtml = ''
    document.getElementById("review_card").innerHTML = cardHtml
    const reviews = await getReviews(book_id);

    for (const review of reviews) {
        cardHtml += `
        <div class="card border-primary mb-3">
            <div class="card-header">
                <p style="font-weight: bold; margin-top: 10px;" class="card-title">${review.fields.user}</p>
                <p style="font-size: xx-small;">Posted on ${review.fields.rating}</p>
            </div>
            <div class="card-body">
                <p class="card-text">${review.fields.review_text}</p>
            </div>
        </div>
        `;
    }

    document.getElementById("review_card").innerHTML = `<div style="margin: 20px" class="card-container" style="display: flex; flex-wrap: wrap; justify-content: space-between;">${cardHtml}</div>`;
}


function post_review(book_id) {
    // const username = document.getElementById("navbarDropdown").innerHTML;
    // document.getElementById("username").value = username;

    const postReviewURL = "post-review/";
    fetch(postReviewURL, {
        method: "POST",
        body: new FormData(document.querySelector('#form')),
    }).then((response) => {
        loadReviews(book_id);
        document.getElementById("form").reset();
    });
}
let card = document.getElementById("review_card")
let book_id = card.getAttribute("data-id")
document.getElementById("create_review_button").onclick = (()=>{post_review(book_id)})
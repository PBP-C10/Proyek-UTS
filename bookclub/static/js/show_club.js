let category =[];

async function getRecommendedBooks(clubId) {
    const recommendedBooksURL = "{% url 'book-club:get_recommended_book_json' 0 %}".replace("0", clubId);
    return fetch(recommendedBooksURL).then((res) => res.json())
}

async function getBubbles(clubId) {
    const bubbleURL = "{% url 'book-club:get_bubble_json' 0 %}".replace("0", clubId);
    return fetch(bubbleURL).then((res) => res.json())
}

function searchBookByCategory(checkbox){
    if (checkbox.checked){
        category.push(checkbox.value)
    } else {
        let indexArr = category.indexOf(checkbox.value)
        if (indexArr != -1){
            category.splice(indexArr, 1)
        }
        page = "1"
    }

    let card = document.getElementById("book_card")
    let clubId = card.getAttribute("data-id")

    loadRecommendedBooks(clubId, category)
}

async function loadRecommendedBooks(clubId, category) {
    let cardHtml = ''
    document.getElementById("book_card").innerHTML = cardHtml
    const recommendedBooks = await getRecommendedBooks(clubId);

    for (const book of recommendedBooks) {
        if (book.fields.category == category || category.length == 0) {
            cardHtml += `
                <div class="col-2 col-sm-2 col-md-2 col-lg-1 col-xl-1 mb-2">
                    <div class="card border-primary h-100" style="width: 100%;">
                        <img src="${book.fields.thumbnail}" class="card-img-top" alt="${book.fields.title}" style="width: 100%; height: auto;">
                        <div class="card-body d-flex flex-column">
                            <h6 class="card-title" style="font-weight: bold;">${book.fields.title}</h6>
                        </div>
                    </div>
                </div>
            `;
        }
    };
    
    document.getElementById("book_card").innerHTML = `
    <div style="margin: 20px; display: flex; flex-wrap: nowrap; overflow-x: auto;">
        ${cardHtml}
    </div>`;
category = [];
}

async function loadBubbles(clubId) {
    let cardHtml = ''
    document.getElementById("bubble_card").innerHTML = cardHtml
    const bubbles = await getBubbles(clubId);

    for (const bubble of bubbles) {
        cardHtml += `
        <div class="card border-primary mb-3">
            <div class="card-header">
                <p style="font-weight: bold; margin-top: 10px;" class="card-title">${bubble.fields.username}</p>
                <p style="font-size: xx-small;">Posted on ${bubble.fields.timestamp}</p>
            </div>
            <div class="card-body">
                <p class="card-text">${bubble.fields.content}</p>
            </div>
        </div>
        `;
    }

    document.getElementById("bubble_card").innerHTML = `<div style="margin: 20px" class="card-container" style="display: flex; flex-wrap: wrap; justify-content: space-between;">${cardHtml}</div>`;
}

function postBubble(clubId) {
    document.getElementById("username").value = "abc";

    const postBubbleURL = "{% url 'book-club:post_bubble' 0 %}".replace("0", clubId);
    fetch(postBubbleURL, {
        method: "POST",
        body: new FormData(document.querySelector('#bubbleForm')),
    }).then((response) => {
        loadBubbles(clubId);
        document.getElementById("bubbleForm").reset();
    });
}

function addRecBook(clubId) {
    const addRecBookURL = "{% url 'book-club:add_rec_book' 0 %}".replace("0", clubId);
    fetch(addRecBookURL, {
        method: "POST",
        body: new FormData(document.querySelector('#recBookForm')),
    }).then((response) => {
        loadRecommendedBooks(clubId, []);
        document.getElementById("recBookForm").reset();
    });
}

let card = document.getElementById("book_card")
let clubId = card.getAttribute("data-id")

loadRecommendedBooks(clubId, [])
loadBubbles(clubId)

document.getElementById("postBubbleButton").onclick = (()=>{postBubble(clubId)})
document.getElementById("addRecBookButton").onclick = (()=>{addRecBook(clubId)})
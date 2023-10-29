async function getClubs() {
    return fetch("{% url 'book-club:get_club_json' %}").then((res) => res.json())
}

async function getBubbles(clubId) {
    return fetch("{% url 'book-club:get_bubble_json' 0 %}").replace("0", clubId).then((res) => res.json())
}

async function getBooks() {
    return fetch("{% url 'book-club:get_book_json' %}").then((res) => res.json())
}

async function loadBooks() {
    const books = await getBooks();

    var recommendedBooks = document.getElementById("recommended_books");
    recommendedBooks.innerHTML = '';

    books.forEach((book) => {
        var option = document.createElement("option");
        option.value = book.pk;
        option.text = book.fields.title;
        recommendedBooks.appendChild(option);
    });
}

async function loadClubs() {
    let cardHtml = ''
    document.getElementById("club_card").innerHTML = cardHtml
    const clubs = await getClubs();

    for (const club of clubs) {
        const isUserOwner = await isOwner(club.pk);
        const isUserMember = await isMember(club.pk);

        cardHtml += `
            <div class="card mx-auto p-1" style="width: 18rem; margin-bottom:10px">
                <div class="card-body">
                    <h5 class="card-title">${club.fields.name}</h5>
                    <p class="card-text" style="font-size: small">${club.fields.description}</p>
                </div>
                <div class="card-body">
                    ${isUserOwner ? 
                        `
                        <button class="btn btn-primary" onclick="showClub(${club.pk})">Show More</button>
                        <button class="btn btn-danger" onclick="deleteClub(${club.pk})">Delete Club</button>
                        ` 
                    : isUserMember ? 
                        `
                        <button class="btn btn-primary" onclick="showClub(${club.pk})">Show More</button>
                        <button class="btn btn-danger" onclick="leaveClub(${club.pk})">Leave</button>
                        ` 
                    : 
                        `
                        <button class="btn btn-primary" onclick="joinClub(${club.pk})">Join</button>
                        `
                    }
                </div>
            </div>
        `;
    };

    document.getElementById("club_card").innerHTML = `<div class="card-container" style="display: flex; flex-wrap: wrap; justify-content: space-between;">${cardHtml}</div>`;
}

function createClub() {
    loadBooks()
    
    fetch("{% url 'book-club:create_club' %}", {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    }).then(loadClubs)

    document.getElementById("form").reset()
    return false
}

function showClub(clubId) {
    window.location.href = `{% url 'book-club:show_club' 0 %}`.replace("0", clubId);
    
    return false
}

function joinClub(clubId) {
    fetch("{% url 'book-club:join_club' 0 %}".replace("0", clubId), {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    }).then(loadClubs)

    document.getElementById("form").reset()
    return false
}

function leaveClub(clubId) {
    fetch("{% url 'book-club:leave_club' 0 %}".replace("0", clubId), {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    }).then(loadClubs)

    document.getElementById("form").reset()
    return false
}

function deleteClub(clubId) {
    fetch("{% url 'book-club:delete_club' 0 %}".replace("0", clubId), {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    }).then(loadClubs)

    document.getElementById("form").reset()
    return false
}

async function isOwner(clubId) {
    let isOwner = false

    const response = await fetch("{% url 'book-club:is_owner' 0 %}".replace("0", clubId), {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    });

    const data = await response.text();

    if (data == 'True') {
        isOwner = true
    }

    return isOwner
}

async function isMember(clubId) {
    let isMember = false

    const response = await fetch("{% url 'book-club:is_member' 0 %}".replace("0", clubId), {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    });

    const data = await response.text();

    if (data == 'True') {
        isMember = true
    }

    return isMember
}

document.getElementById("createClubButton").onclick = loadBooks
loadClubs()
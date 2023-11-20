function addFilterComponent(){
    let filterString = 
        `
        <div class="d-flex flex-row justify-content-between align-items-center">
            <h5 class="my-auto">Category</h5>
            <button class="btn btn-sm" type="button" data-bs-toggle="collapse" data-bs-target="#collapseCategory" aria-expanded="false" aria-controls="collapseExample">
                <i class="bi bi-caret-down-fill" ></i>
            </button>
        </div>
        <div class="collapse" id="collapseCategory">
            <div class="container my-2" id="categoryContainer">
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" id="checkboxAdvStories" value="Adventure stories" onchange=searchBookByCategory(this)>
                    <label class="form-check-label" for="checkboxAdvStories">
                        Adventure Stories
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" id="checkboxArt" value="Art" onchange=searchBookByCategory(this)>
                    <label class="form-check-label" for="checkboxArt">
                        Art
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" id="checkboxComics" value="Comics & Graphic Novels" onchange=searchBookByCategory(this)>
                    <label class="form-check-label" for="checkboxComics">
                        Comics & Graphic Novels
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" id="checkboxDetective" value="Detective and mystery stories" onchange=searchBookByCategory(this)>
                    <label class="form-check-label" for="checkboxDetective">
                        Detective and Mystery Stories
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" id="checkboxDrama" value="Drama" onchange=searchBookByCategory(this)>
                    <label class="form-check-label" for="checkboxDrama">
                        Drama
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" id="checkboxFantasy" value="Fantasy fiction" onchange=searchBookByCategory(this)>
                    <label class="form-check-label" for="checkboxFantasy">
                        Fantasy Fiction
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" id="checkboxHistory" value="History" onchange=searchBookByCategory(this)>
                    <label class="form-check-label" for="checkboxHistory">
                        History
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" id="checkboxJuvenile" value="Juvenile Fiction" onchange=searchBookByCategory(this)>
                    <label class="form-check-label" for="checkboxJuvenile">
                        Juvenile Fiction
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" id="checkboxScience" value="Science fiction" onchange=searchBookByCategory(this)>
                    <label class="form-check-label" for="checkboxScience">
                        Science Fiction
                    </label>
                </div>
                
            </div>
        </div>
        <hr class="hr m-1">
        <div class="d-flex flex-row justify-content-between align-items-center">
            <h5 class="my-auto">Price</h5>
            <button class="btn btn-sm" type="button" data-bs-toggle="collapse" data-bs-target="#collapsePrice" aria-expanded="false" aria-controls="collapseExample">
                <i class="bi bi-caret-down-fill" ></i>
            </button>
        </div>  
        <div class="collapse" id="collapsePrice">
            <div class="container my-2" id="priceContainer">
                <div class="input-group mb-3">
                    <span class="input-group-text">Rp</span>
                    <input type="number" class="form-control" placeholder="Min Price" oninput=filterHarga() id="minPriceBox" min="0" max="500000">
                </div>
                <div class="input-group mb-3">
                    <span class="input-group-text">Rp</span>
                    <input type="number" class="form-control" placeholder="Max Price" oninput=filterHarga() id="maxPriceBox" min="0" max="500000">
                </div>
            </div>
        </div>
        <hr class="hr m-1">
        <div class="d-flex flex-row justify-content-between align-items-center">
            <h5 class="my-auto">Rating</h5>
            <button class="btn btn-sm" type="button" data-bs-toggle="collapse" data-bs-target="#collapseRating" aria-expanded="false" aria-controls="collapseExample">
                <i class="bi bi-caret-down-fill" ></i>
            </button>
        </div> 
        <div class="collapse" id="collapseRating">
            <div class="container my-2 d-flex flex-column" id="ratingContainer">

                <input type="radio" class="btn-check" name="options" id="star2" autocomplete="off" onchange=filterRating(this) value="4">
                <label class="btn" for="star2">
                    <i class="bi bi-star-fill"></i> <i class="bi bi-star-fill"></i> <i class="bi bi-star-fill"></i> <i class="bi bi-star-fill"></i> <i class="bi bi-star"></i> and up
                </label>

                <input type="radio" class="btn-check" name="options" id="star3" autocomplete="off" onchange=filterRating(this) value="3">
                <label class="btn" for="star3">
                    <i class="bi bi-star-fill"></i> <i class="bi bi-star-fill"></i> <i class="bi bi-star-fill"></i> <i class="bi bi-star"></i> <i class="bi bi-star"></i> and up
                </label>

                <input type="radio" class="btn-check" name="options" id="star4" autocomplete="off" onchange=filterRating(this) value="2">
                <label class="btn" for="star4">
                    <i class="bi bi-star-fill"></i> <i class="bi bi-star-fill"></i> <i class="bi bi-star"></i> <i class="bi bi-star"></i> <i class="bi bi-star"></i> and up
                </label>

                <input type="radio" class="btn-check" name="options" id="star5" autocomplete="off" onchange=filterRating(this) value="1">
                <label class="btn" for="star5">
                    <i class="bi bi-star-fill"></i> <i class="bi bi-star"></i> <i class="bi bi-star"></i> <i class="bi bi-star"></i> <i class="bi bi-star"></i> and up
                </label>

                <input type="radio" class="btn-check" name="options" id="clearRating" autocomplete="off" onchange=filterRating(this) value="0">
                <label class="btn" for="clearRating">
                    No Filter
                </label>
            </div>
        </div>`

    document.getElementById('offcanvasRating').innerHTML = filterString
    document.getElementById('filterContainer').innerHTML = filterString
}

addFilterComponent()

async function getBooks(category, filter, page, minPrice, maxPrice, minRating) {
    let url = new URL("get-books", window.location)
    let param = new URLSearchParams(url.search)
    if (page > 1){
        param.append('page', page)
    }
    if (category.length != 0){
        param.append('category', category)
    }
    if (filter != ""){
        param.append("filter", filter)
    }
    if (minPrice != 0){
        param.append("minPrice", minPrice)
    }
    if (maxPrice < 500000){
        param.append("maxPrice", maxPrice)
    }
    if (minRating > 0){
        param.append("minRating", minRating)
    }
    url = new URL(url.href + "/?" + param)
    return fetch(url).then((res) => res.json())
}

async function refreshPage(category, filter, page, minPrice, maxPrice, minRating) {
    const booksData = await getBooks(category, filter, page, minPrice, maxPrice, minRating)
    let bookCardString = '<div class="row row-cols-2 row-cols-sm-3 row-cols-md-4 row-cols-lg-5">'
    let pageString = '<ul class="pagination">'
    books = JSON.parse(booksData.books)
    if (books.length == 0){
        bookCardString = 
            `<div class="container-fluid text-center">
                <h1 class="text-center"> No Books Found</h1>
                <br>
                <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#bookRequestModal" id="reqButtonNotFound">Request a Book</button>
            </div>`
        pageString = ""
    } else {
        books.forEach((book) => {
            book.fields.ratings_count = book.fields.ratings_count > 1000 ? Math.floor(book.fields.ratings_count / 1000) + "k+" : book.fields.ratings_count
            if (book.fields.subtitle != ""){
                book.fields.subtitle = ": " + book.fields.subtitle
            }
            bookCardString += 
                `<div class="col my-2">
                    <div class="card shadow rounded h-100" onclick=getDetail(this) id=${book.pk}>
                        <img src="${book.fields.thumbnail}" alt="" class="card-img-top h-50" loading="lazy">
                        <div class="card-body d-flex flex-column p-2 h-50">
                            <h6 class="card-title mb-2 text-truncate-2 lh-2">${book.fields.title}${book.fields.subtitle}</h6>
                            <h6 class="card-text mb-2 text-muted text-truncate-2">${book.fields.author}</h6>
                            <h6 class="card-text mb-2">Rp ${book.fields.price}</h6>
                            <h6 class="card-text mb-2"><i class="bi bi-star-fill"></i> ${book.fields.average_rating}</h6> 
                            <h6 class="card-text mb-2">${book.fields.ratings_count} ratings</h6>
                        </div>
                    </div>
                </div>`
        })

        totalPageNum = JSON.parse(booksData.total_page_num)
        currentPage = JSON.parse(booksData.current_page)
        hasNext = JSON.parse(booksData.has_next)
        nextPage = JSON.parse(booksData.next_page)
        prevPage = JSON.parse(booksData.prev_page)
        hasPrev = JSON.parse(booksData.has_previous)
        
        for (let i = 0; i <= totalPageNum + 1; i++){
            if (i == 0){
                if (hasPrev){
                    pageString += `<li class="page-item"><a class="page-link" onclick=goToPage(${prevPage})>Previous</a></li>`
                } else {
                    pageString += `<li class="page-item disabled"><a class="page-link" href="#">Previous</a></li>`
                }
            } else if (i == totalPageNum + 1){
                if (hasNext){
                    pageString += `<li class="page-item"><a class="page-link" onclick=goToPage(${nextPage}) >Next</a></li>`
                } else {
                    pageString += `<li class="page-item disabled"><a class="page-link" href="#">Next</a></li>`
                }
            } else if (i == currentPage){
                pageString += `<li class="page-item active"><a class="page-link active" href="#">${i}</a></li>`
            } else {
                pageString += `<li class="page-item"><a class="page-link" onclick=goToPage(${i})>${i}</a></li>`
            }
        }
    
        
        bookCardString += '\n</div>'
        pageString += `\n</ul>`
    }

        document.getElementById("book_cards").innerHTML = bookCardString
        document.getElementById("page").innerHTML = pageString
}

let filter = document.getElementById("search").value
let category = []
let page = "1"
let minPrice = 0
let maxPrice = 500000
let minRating = 0

refreshPage(category, filter, page, minPrice, maxPrice, minRating)

function goToPage(newPage){
    page = newPage
    refreshPage(category, filter, page, minPrice, maxPrice, minRating)
    window.scrollTo(0,0)
}

function searchBook(){
    filter = document.getElementById("search").value
    refreshPage(category, filter, page, minPrice, maxPrice)
}

function searchBookByCategory(checkbox){
    filter = document.getElementById("search").value
    if (checkbox.checked){
        category.push(checkbox.value)
    } else {
        let indexArr = category.indexOf(checkbox.value)
        if (indexArr != -1){
            category.splice(indexArr, 1)
        }
        page = "1"
    }
    refreshPage(category,filter,page, minPrice, maxPrice, minRating)
}

function filterHarga(){
    filter = document.getElementById("search").value
    minPrice = document.getElementById("minPriceBox").value
    maxPrice = document.getElementById("maxPriceBox").value
    refreshPage(category,filter,page,minPrice,maxPrice, minRating)
}

function filterRating(radio){
    filter = document.getElementById("search").value
    if (radio.checked){
        minRating = parseInt(radio.value)
    } else {
        radio.checked = false
        minRating = 0
    }
    refreshPage(category,filter,page,minPrice,maxPrice, minRating)
}

function getDetail(book){
    window.location = new URL('detail/' + book.id, window.location)
}

function requestBook() {
    let url = new URL("request-book/", window.location)
    fetch(url, {
        method: "POST",
        body: new FormData(document.querySelector('#request-form'))
    }).then((res) => {
        const requestModal = document.querySelector('#bookRequestModal')
        const requestModalBootstrap = bootstrap.Modal.getInstance(requestModal)
        const loginToast = document.querySelector('#loginToast')
        const loginToastBootstrap = bootstrap.Toast.getOrCreateInstance(loginToast)
        const formValidationToast = document.querySelector('#formValidationToast')
        const formValidationToastBootstrap = bootstrap.Toast.getOrCreateInstance(formValidationToast)
        const successToast = document.querySelector('#successToast')
        const successToastBootstrap = bootstrap.Toast.getOrCreateInstance(successToast)
       
        if (res.status == 201){
            successToastBootstrap.show()
            document.getElementById("request-form").reset()
            requestModalBootstrap.hide()
        } else if (res.status == 401){
            loginToastBootstrap.show()
        } else if (res.status == 400){
            formValidationToastBootstrap.show()
        }
    })
}

async function getBookRequests(){
    return fetch('get-book-requests/').then((res) => res.json())
}

async function refreshBookRequest(){
    const bookRequests = await getBookRequests()
    let bookRequestString = ""
    if (bookRequests.length == 0){
        bookRequestString = `
        <div class="card my-2">
            <div class="card-body">
                <strong>You have no Book Request</strong>
            </div>
        </div>
        `
    } else {
        bookRequests.forEach((bookRequest) => {
            bookRequestString += `
            <div class="card my-2">
                <div class="card-body">
                    <div class="row">
                        <div class="col">
                            <h5 class="card-title">Book Title: ${bookRequest.fields.title}</h5>
                            <h6 class="card-text mb-2">Author: ${bookRequest.fields.author}</h6>
                            <h6 class="card-text mb-2">Category: ${bookRequest.fields.category}</h6>
                            <h6 class="card-text mb-2">Status: ${bookRequest.fields.status}</h6>
                        </div>
                        <div class="col text-end">
                            <button type="button" class="btn btn-danger" onclick=deleteBookRequest(${bookRequest.pk})>Delete</button>
                        </div>
                    </div>
                </div>
            </div>
            `
        })
    }

    document.getElementById("myBookRequestModalBody").innerHTML = bookRequestString
}

async function deleteBookRequest(id){
    fetch('delete-book-request/' + id + '/').then(refreshBookRequest)
}

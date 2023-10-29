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
    let bookCardString = '<div class="row row-cols-1 row-cols-md-5">'
    let pageString = '<ul class="pagination">'
    books = JSON.parse(booksData.books)
    if (books.length == 0){
        bookCardString = 
            `<img src="https://us-tuna-sounds-images.voicemod.net/728d9e58-0390-4f53-9de1-61466c055da8-1691346150925.png" loading="lazy" class="rounded mx-auto d-block">
            <h1 class="text-center"> ATTN: FIX THIS AS SOON AS POSSIBLE!!</h1>
            <h1 class="text-center"> NO BOOKS!!!</h1>
            <h1 class="text-center"> I have spoken! This is the way! </h1>
            `
        pageString = ""
    } else {
        books.forEach((book) => {
            book.fields.ratings_count = book.fields.ratings_count > 1000 ? Math.floor(book.fields.ratings_count / 1000) + "k+" : book.fields.ratings_count
            if (book.fields.subtitle != ""){
                book.fields.subtitle = ": " + book.fields.subtitle
            }
            bookCardString += 
                `<div class="col col-auto my-2">
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
        if (res.status == 201){
            document.getElementById("request-form").reset()
            const requestModal = document.querySelector('#bookRequestModal')
            const modal = bootstrap.Modal.getInstance(requestModal)
            modal.hide()
        } else if (res.status == 401){
            
        }
    })
}

let reqButton = document.getElementById("reqButtonDiv")


reqButton.onclick = function() {
    reqButton.style.width = '200px'
    let timer = setTimeout( function() {
        document.getElementById("reqButton").innerHTML = `<p class="container-fluid text-center m-0">Missing a Book? <br> Request New Book</p>`
    }, 200)
    reqButton.onmouseout = function() {
        reqButton.style.width = '75px'
        document.getElementById("reqButton").innerHTML = `<h3 class="container-fluid text-center m-0"><i class="bi bi-plus"></i></h3>`
        clearTimeout(timer)
    }
}


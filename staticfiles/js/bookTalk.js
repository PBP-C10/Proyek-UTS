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
            `<h1 class="text-center"> No books are found</h1> `
        pageString = ""
    } else {
        books.forEach((book) => {
            bookCardString += 
            // `<div class="col col-auto my-2">
            //     <div class="card shadow rounded h-100" onclick="getDetail(this)" id="${book.pk}">
            //         <div class="card-body d-flex flex-column p-2 h-100">
            //             <h6 class="card-title mb-2 text-truncate-2 lh-2">Review ${book.fields.title}</h6>
            //             <h6 class="card-text mb-2 text-muted text-truncate-2">${book.fields.author}</h6>
            //         </div>
            //     </div>
            // </div>`

            `<div class="container">
                <div class="col col-auto my-2">
                    <div class="card-header shadow" onclick="getDetail(this)" id="${book.pk}"
                        <p style="font-weight: bold; margin-top: 10px;" class="card-title">Review of "${book.fields.title}"</p>
                        <p style="font-size: xx-small;">${book.fields.author}</p>
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

function getDetail(card) {
    window.location = new URL('book/' + card.id, window.location);
}


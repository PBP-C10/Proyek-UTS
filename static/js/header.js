let pathname = window.location.pathname
if (pathname == "/"){
    document.getElementById("bookfinds-nav").classList.add("active")
} else if (pathname == "/book-club/"){
    document.getElementById("bookclub-nav").classList.add("active")
} else if (pathname == "/BookShop/shopping-main/"){
    document.getElementById("bookshop-nav").classList.add("active")
} else if (pathname == "/book-talk/"){
    document.getElementById("booktalk-nav").classList.add("active")
}
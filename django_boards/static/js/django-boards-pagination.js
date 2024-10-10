function paginationScrollBehavior() {
  document.querySelector('.page-link', function (e) {
    e.preventDefault()
  }).scrollIntoView({
    behavior: "smooth", block: "end", inline: "nearest"
  })
}

// paginationScrollBehavior()

export default paginationScrollBehavior


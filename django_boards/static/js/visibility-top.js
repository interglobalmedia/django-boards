// scroll top button disappears after click when scrollY == 0, but it reappears when scrollY is greater than 0 on scroll down.
function toggleVisibilityScrollTop() {
  document.addEventListener('scroll', function () {
    const scrollButton = document.querySelector('.scroll.top')
    if (window.scrollY > 0) {
      scrollButton.style.opacity = 1
      scrollButton.style.transition = 'opacity 1s ease'
    } else {
      scrollButton.style.opacity = 0
      scrollButton.style.transition = 'opacity 1s ease'
    }
  })
}

export default toggleVisibilityScrollTop
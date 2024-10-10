// scroll bottom button disappears after click of the scroll top button when scrollY == 0, but it reappears when scrollY is greater than 0 on scroll down.
function toggleVisibilityScrollBottom() {
  document.addEventListener('scroll', function () {
    const scrollButton = document.querySelector('.scroll.bottom')
    if (window.scrollY > 0) {
      // CSS in JS to change opacity from 0 (app.css) to 1
      scrollButton.style.opacity = 1
      scrollButton.style.transition = 'opacity 1s ease'
    } else {
      // CSS in JS to change opacity from 1 to 0
      scrollButton.style.opacity = 0
      scrollButton.style.transition = 'opacity 1s ease'
    }
  })
}

export default toggleVisibilityScrollBottom
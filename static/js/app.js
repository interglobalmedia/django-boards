import {
  scrollTopButton,
  scrollFunction,
  backToTop,
} from './scroll-top.js'

// When the user scrolls down 20px from the top of the document, show the button. This must come first.
window.onscroll = function () {
  scrollFunction()
}

// When the user clicks on the button, scroll to the top of the document. This must come after window.onscroll, otherwise it will not work.
scrollTopButton.addEventListener("pointerdown", backToTop)

// inits
const url = document.location.href;

const copyButton = new Clipboard('.copy-button', {
  text: function () {
    return url
  }
})

// added July 10, 2026. Mentioned in Fullstack Django Application Part 22.
let paginationBody = document.querySelector('.page-item');
if (paginationBody) {
  paginationBody.scrollIntoView()
}

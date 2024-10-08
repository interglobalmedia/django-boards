// For scroll to top functionality
const scrollTopButton = document.querySelector('.scroll.top')

function scrollTop() {
	window.scrollTo(0, 0)
}

scrollTopButton.addEventListener('click', scrollTop)

// Scroll to bottom functionality
const scrollDownButton = document.querySelector('.scroll')

function scrollStep() {
	window.scroll(0, window.scrollY + 200)
	console.log(window.scrollY + 200)
}

scrollDownButton.addEventListener('pointerdown', scrollStep)

// scroll top button disappears after click when scrollY == 0, but it reappears when scrollY is greater than 0 on scroll down.
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

// scroll bottom button disappears after click of the scroll top button when scrollY == 0, but it reappears when scrollY is greater than 0 on scroll down.
document.addEventListener('scroll', function () {
	const scrollButton = document.querySelector('.scroll.bottom')
	if (window.scrollY > 0) {
		scrollButton.style.opacity = 1
		scrollButton.style.transition = 'opacity 1s ease'
	} else {
		scrollButton.style.opacity = 0
		scrollButton.style.transition = 'opacity 1s ease'
	}
})

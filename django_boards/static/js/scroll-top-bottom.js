// For scroll to top functionality
export const scrollTopButton = document.querySelector('.scroll.top')

export function scrollTop() {
	window.scrollTo(0, 0)
}

scrollTopButton.addEventListener('pointerdown', scrollTop)

// Scroll to bottom functionality
export const scrollDownButton = document.querySelector('.scroll')

export function scrollStep() {
	window.scroll(0, window.scrollY + 200)
	console.log(window.scrollY + 200)
}

scrollDownButton.addEventListener('pointerdown', scrollStep)

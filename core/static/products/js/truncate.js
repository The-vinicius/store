const titulo = document.querySelectorAll('.truncate');

let truncate = function (elem, limit, text) {
	
	// Make sure an element and number of items to truncate is provided
	if (!elem || !limit) return;

	// Get the inner content of the element
	var content = text
	content = content.trim();

	// if length lt limit return true
	if (content.split(' ').length < limit) {
		return true;
	}

	// Convert the content into an array of words
	// Remove any words above the limit
	content = content.split(' ').slice(0, limit);

	// Convert the array of words back into a string
	// If there's content to add after it, add it
	content = content.join(' ') + '...'
	// Inject the content back into the DOM
	if (elem.textContent) {
		elem.textContent = content;
	} else {
		elem.innerText = content;
	}

};

// original name products
function desktop(elem, texto) {
	if (elem.textContent) {
		elem.textContent = texto;
	} else {
		elem.innerText = texto;
	}
}

// list with name product
const textList = []
for (let i = 0; i < titulo.length; i++) {
	textList.push(titulo[i].textContent)
}


function mobile() {
	if (window.innerWidth < 768) {
		let elems = document.querySelectorAll('.truncate');
		for (let i = 0; i < elems.length; i++) {
			truncate(elems[i], 7, textList[i])
		}

	} else {
		let elems = document.querySelectorAll('.truncate');
		for (let i = 0; i < elems.length; i++) {
			desktop(elems[i], textList[i])
		}
	}
};

// listener size screen
window.addEventListener('resize', mobile)

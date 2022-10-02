
let truncate = function (elem, limit) {
	
	// Make sure an element and number of items to truncate is provided
	if (!elem || !limit) return;

	// Get the inner content of the element
	var content = elem.textContent || elem.innerText;
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


if (screen.width < 700 ) {
	console.log(screen.width);
	let elems = document.querySelectorAll('.truncate');
	for (let i = 0; i < elems.length; i++) {
		truncate(elems[i], 7)
	}
};


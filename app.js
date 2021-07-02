const updateCounts = (textValue, wordCountBanner, charCountBanner) =>{
	const words = textValue.split(" ");
	const chars = textValue.split("").filter((char) => char !== " "); // eliminate spaces -- do not want to count these in char count
	wordCountBanner.textContent = words.length; 
	charCountBanner.textContent = chars.length; 
}

window.onload = (event) =>{
	const textContainer = document.getElementById("word-input-area");
	const clear = document.getElementById("clear-button"); 
	const copy = document.getElementById("select-button");
	const find = document.getElementById("find-button"); 
	const replace = document.getElementById("replace-button"); 
	const findBanner = document.getElementById("find-banner");
	const findInput = document.getElementById("find-input");
	const replaceInput = document.getElementById("replace-input"); 
	// add styling to the textContainer 
	textContainer.style.margin = "auto";
	textContainer.style.width = '40%'; 
	textContainer.style.border = "3px solid #73AD21";
	textContainer.style.padding = "10px";

	// add event listener to textarea 
	const text = document.getElementById("text-area");
	const wordCount = document.getElementById('word-count'); 
	const charCount = document.getElementById("char-count");
	const defaultText = "Start Typing...";

	// event listeners 
	text.addEventListener('input', (event) =>{

		updateCounts(text.value, wordCount, charCount); 

	}); 
	text.addEventListener('click', (event) =>{
		if (text.value === defaultText){
			text.value = ""; 
		}

	});

	clear.addEventListener("click", (event) =>{
		text.value = "";
		wordCount.textContent = 0;
		charCount.textContent = 0;  
	}); 
	copy.addEventListener("click", (event) =>{
		if (text.value){
			text.select(); 
			document.execCommand("copy"); 
		}
		else{
			alert("No text to be copied...."); 
		}

	});

	find.addEventListener("click", (event) =>{
		if (findInput.value === ""){
			findBanner.textContent = "No input to find.";
			return;  
		}
		const wordToFind = findInput.value; 
		const numOccurences = text.value.toLowerCase().split(wordToFind.toLowerCase()).length - 1;// -1 because the word will be 'joining' this array
		findBanner.textContent = `Found ${numOccurences} instances of ${wordToFind}.`; 
	});

	replace.addEventListener("click", (event) =>{
		const wordToFind = findInput.value; 
		const wordToReplace = replaceInput.value; 
		const numOccurences = text.value.toLowerCase().split(wordToFind.toLowerCase()).length - 1;
		// not sure how to do this without altering the capitalizations of the text.... 
		text.value = text.value.toLowerCase().split(wordToFind.toLowerCase()).join(wordToReplace);  // replace the word 
		findBanner.textContent = `Replaced ${numOccurences} instances of '${wordToFind}' with '${wordToReplace}'.`;
		// // update word counts 
		updateCounts(text.value, wordCount, charCount);
	})



}

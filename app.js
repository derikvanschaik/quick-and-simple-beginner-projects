window.onload = (event) =>{
	const textContainer = document.getElementById("word-input-area");
	const clear = document.getElementById("clear-button"); 
	const copy = document.getElementById("select-button"); 
	// add styling to the textContainer 
	textContainer.style.margin = "auto";
	textContainer.style.width = '30%'; 
	textContainer.style.border = "3px solid #73AD21";
	textContainer.style.padding = "10px";

	// add event listener to textarea 
	const text = document.getElementById("text-area");
	const wordCount = document.getElementById('word-count'); 
	const charCount = document.getElementById("char-count");
	const defaultText = "Start Typing...";

	// event listeners 
	text.addEventListener('input', (event) =>{
		const words = text.value.split(" ");
		wordCount.textContent = words.length;
		const chars = text.value.split("").filter((char) => char !== " "); // eliminate spaces -- do not want to count these in char count
		console.log(chars); 
		charCount.textContent = chars.length; 

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


}

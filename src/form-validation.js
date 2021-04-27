function boxChecked() {
	const radioGroups = document.querySelectorAll("crowd-radio-group");
	let valid = true;
	for (let radioGroup of radioGroups) {
		let validGroup = false;
		let radioButtons = radioGroup.children;
		for (let radioButton of radioButtons) {
			validGroup = validGroup || radioButton.checked;
		}
		valid = valid && validGroup;
	}
	return valid;
}

//from https://stackoverflow.com/questions/54266891/submission-validation-with-the-crowd-template-on-mturk
window.onload = function() {
	document.querySelector('crowd-form').onsubmit = function(e) {
		if (!boxChecked()) {
			alert("Please answer all the questions before submitting.");
			e.preventDefault();
		}
	}
}
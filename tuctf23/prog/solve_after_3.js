for (let i = 0; i < 151; i++) {
	document.querySelector('input[name="word"]').value = document.querySelector('strong[name="word-title"]').innerText;
	document.querySelector('button[type="submit"]').click();
	await new Promise(r => setTimeout{() => r(), 550});
}

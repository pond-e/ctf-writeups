for(let i = 0; i < 150; i++) {
var wordTitleElement = document.querySelector('strong[name="word-title"]');
var ad = document.querySelector('input[name="word"]');
ad.value = wordTitleElement.innerText;
document.querySelector.onsubmit = function(event){event.preventDefault();};
var form = document.querySelector('form');
form.submit();
}

setInterval(() => {
    content = document.querySelector("#beans").innerHTML
    document.querySelector("#in").value = content
    document.forms[0].requestSubmit(document.querySelector("#sub"))
}, 300)

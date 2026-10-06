function checkUser(){
    username = document.querySelector("#inputUsername").value.trim()
    fetch(`/checkUser?usernameCheck=${encodeURIComponent(username)}`)
    
}
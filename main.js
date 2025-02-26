// const username = document.getElementById('username').value;
// const email = document.getElementById('email').value;
// const password = document.getAnimations('password').value;
// const passwordConfirmation = document.getElementById('passwordConfirmation').value;

// if (username && email && password && passwordConfirmation) {
//     if (password === passwordConfirmation) {
//         const response = fetch('register', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json'
//             },
//             body: JSON.stringify({
//                 username,
//                 email,
//                 password
//             })
//         })
//        const data = response.json()
//        if (response.ok) {
//             window.location.href = '/login';
//        }
//     } else {
//         alert('Passwords do not match!');
//     }
// }


const username = document.getElementById('username').value;
const password = document.getAnimations('password').value;


if (username  && password ) {
    if (password === username ) {
        const response = fetch('login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username,
                password
            })
        })
       const data = response.json()
       if (response.ok) {
            window.location.href = '/';
            localStorage.setItem("access_token", data.access_token)
            localStorage.setItem("username", data.data.username)
            localStorage.setItem("email", data.data.email)
            localStorage.setItem("id", data.data.id)
       }
    } else {
        alert('Passwords do not match!');
    }
}
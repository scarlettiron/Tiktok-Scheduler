login_btn = document.getElementById('login-btn')
signup_btn = document.getElementById('signup-btn')
signup_fields = document.getElementById('signup-fields')


//for switching form fields between login and signup
const switch_active_fields = () =>{
    if(signup_fields.classList.contains('form-inactive')){
        signup_fields.classList.add('form-active')
        signup_fields.classList.remove('form-inactive')
        login_btn.classList.remove('unmuted')
        signup_btn.classList.add('unmuted')
        return
    }

    signup_fields.classList.add('form-inactive')
    signup_fields.classList.remove('form-active')   
    signup_btn.classList.remove('unmuted')
    login_btn.classList.add('unmuted')
}

signup_btn.addEventListener('click', switch_active_fields)
login_btn.addEventListener('click', switch_active_fields)
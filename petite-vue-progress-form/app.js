const app = PetiteVue.createApp({
    $delimiters: ['${', '}'],
    isSubmitting: false,
    // progress trackers
    _fname: 0,
    _lname: 0,
    _email: 0,
    _password: 0,
    _re_password: 0,
    // form fields
    first_name: "",
    last_name: "",
    email: "",
    password: "",
    confirm_password: "",
    // dynamic submit button items
    submitContent: "Register&nbsp;&nbsp;<span class='fa fa-arrow-right'></span>",
    // form message
    formMessage: "",

    // computed methods
    get progressPercentage() {
        return this._fname + this._lname + this._re_password + this._password + this._email
    },
    get lastNameError () {
        if(this._validName(this.last_name)) {
            this._lname = 20
            return ""
        } else {
            this._lname = 0
            return "Last name can only contain letters, spaces and must be more than 2 characters."
        }
    },
    get firstNameError() {
        if(!this._validName(this.first_name)) {
            this._fname = 20
            return ""
        } else {
            this._fname = 0
            return "First name can only contain letters, spaces and must be more than 2 characters."
        }
    },
    get emailError() {
        if(!this._validEmail()) {
            this._email = 0
            return "Looks like your email address is not valid."
        }
        this._email = 30
        return ""
    },
    get passwordError() {
        if(this.password.length < 6) {
            this._password = 0
            return "Password can not be less than 6 characters."
        }
        this._password = 15
        return ""
    },
    get rePasswordError() {
        if(this.confirm_password.length < 6){
            this._re_password  = 0
            return "Required field."
        }else if(this.password !== this.confirm_password) {
            this._re_password  = 0;
            return "Password didn't match."
        }
        this._re_password = 15
        return ""
    },

    // validators
    _validName(name) {
        let _regex = /^([a-zA-Z ]{3,})$/
        return Boolean(name.match(_regex))
    },
    _validEmail() {
        let res = Boolean(String(this.email)
            .toLowerCase()
            .match(
                /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            ))
        return res
    },
    
    // form methods
    _resetForm() {
        this.password = ""
        this.email = ""
        this.first_name = ""
        this.last_name = ""
        this.confirm_password = ""
    },
    submitForm() {
        if(this.isSubmitting) return
        this.formMessage = ""
        this.isSubmitting = true
        // pretend like the API call went well :P
        setTimeout(() => {
            this.formMessage = "<b>Congrats!</b> You are successfully registered."
            this.isSubmitting = false
            // reset form
            this._resetForm()
        }, 1500)
    },
})


app.mount("#app")

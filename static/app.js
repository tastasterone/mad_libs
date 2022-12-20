const form = document.querySelector('#story-form')
const place = document.querySelector('#place')
const noun = document.querySelector('#noun')
const verb = document.querySelector('#verb')
const adj = document.querySelector('#adjevtive')
const plurNoun = document.querySelector('#plural_noun')
const errorMsg = document.querySelector('.error-message')

form.addEventListener('submit', function(){
    if (!place && !noun && !verb && !adj && !plurNoun) {
        errorMsg.display = 'block'
    }
})
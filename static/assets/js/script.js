const formContainer = document.querySelector(".forms"), // Renamed to formContainer to avoid conflict
      pwShowHide = document.querySelectorAll(".eye-icon"),
      links = document.querySelectorAll(".link");

pwShowHide.forEach(eyeIcon => {
    eyeIcon.addEventListener("click", () => {
        let pwFields = eyeIcon.parentElement.parentElement.querySelectorAll(".password");
        
        pwFields.forEach(password => {
            if(password.type === "password"){
                password.type = "text";
                eyeIcon.classList.replace("bx-hide", "bx-show");
                return;
            }
            password.type = "password";
            eyeIcon.classList.replace("bx-show", "bx-hide");
        });
        
    });
});      

links.forEach(link => {
    link.addEventListener("click", e => {
       e.preventDefault(); // Preventing form submit
       formContainer.classList.toggle("show-signup");
    });
});

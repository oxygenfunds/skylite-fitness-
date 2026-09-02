"use strict";



console.log("Hello World!");



console.log("🔥 JS CONNECTED");




// const sections = document.querySelectorAll(".box-left, .box-right");

// sections.forEach(section => {

//     const divs = section.querySelectorAll(".box")

//     const sectionObserver = new IntersectionObserver(

//       (knox)=> {

//         knox.forEach(knox => {
//             if(knox.isIntersecting) {

//                 divs.forEach ((boxes, index ) => {
//                     setTimeout(( ) => boxes.classList.add("show"), index * 400 );
//                 })
                
//             }else {
//                  boxes.forEach(divs => divs.classList.remove("show"))
//             }
//         })
// }
// ,{treshold:0.5});

// sectionObserver.observe(section);
// });



// const sectionObserver = new IntersectionObserver(

//       ()=> {

// }
// ,{treshold:0.2});

// alert("Hello World!");


// document.getElementById("contact-form").addEventListener("submit",


// document.addEventListener("DOMContentLoaded", function()  {
    
//     console.log("DOM fully loaded and parsed");

//     const form = document.getElementById("contact-form");

//     if (form) { 
//         form.addEventListener("submit",function(e) {
//             event.preventDefault();
//             alert("Form submitted!");
// })

//      emailjs.sendForm(
//         "YOUR_SERVICE_ID",
//         "YOUR_TEMPLATE_ID",
//         this
//     ).then(function() {

//         // show success message
//         document.getElementById("success-msg").classList.remove("d-none");

//         // clear form
//         document.getElementById("contact-form").reset();

//     }, function(error) {
//         alert("Failed to send message 😢");
//     });

    
// } )    



// document.addEventListener("DOMContentLoaded", function () {

//     console.log("🔥 JS Loaded Successfully");

//     const form = document.getElementById("contact-form");

//     if (form) {

//         form.addEventListener("submit", function (e) {
//             e.preventDefault();  // stop page refresh

//             console.log("Form submitted 🚀");

//             emailjs.sendForm(
//                 "service_mf6ek3e",
//                 "template_mbfjsso",
//                 this
//             ).then(function () {

//                 // show success message
//                 document.getElementById("success-msg").classList.remove("d-none");

//                 // clear form
//                 form.reset();

//             }, function (error) {
//                 console.log(error);
//                 alert("Failed to send message 😢");
//             });

//         });

//     }



const accordionHeaders = document.querySelectorAll(".accordion-header");

accordionHeaders.forEach((header) => {

    header.addEventListener("click", () => {

        const body = header.nextElementSibling;

        header.classList.toggle("active");

        if (body.style.maxHeight) {
            body.style.maxHeight = null;
        } else {
            body.style.maxHeight = body.scrollHeight + "px";
        }

    });

});

    
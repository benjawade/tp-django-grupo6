'use strict';

/**
 * add event listener on multiple elements
 */

const addEventOnElements = function (elements, eventType, callback) {
  for (let i = 0, len = elements.length; i < len; i++) {
    elements[i].addEventListener(eventType, callback);
  }
}

/**
 * PRELOADER
 * 
 * preloader will be visible until document load
 */

const preloader = document.querySelector("[data-preloader]");

window.addEventListener("load", function () {
  preloader.classList.add("loaded");
  document.body.classList.add("loaded");
});

/**
 * MOBILE NAVBAR
 * 
 * show the mobile navbar when click menu button
 * and hidden after click menu close button or overlay
 */

const navbar = document.querySelector("[data-navbar]");
const navTogglers = document.querySelectorAll("[data-nav-toggler]");
const overlay = document.querySelector("[data-overlay]");

const toggleNav = function () {
  navbar.classList.toggle("active");
  overlay.classList.toggle("active");
  document.body.classList.toggle("nav-active");
}

addEventOnElements(navTogglers, "click", toggleNav);

/**
 * HEADER & BACK TOP BTN
 * 
 * active header & back top btn when window scroll down to 100px
 */

const header = document.querySelector("[data-header]");
const backTopBtn = document.querySelector("[data-back-top-btn]");

const activeElementOnScroll = function () {
  if (window.scrollY > 100) {
    header.classList.add("active");
    backTopBtn.classList.add("active");
  } else {
    header.classList.remove("active");
    backTopBtn.classList.remove("active");
  }
}

window.addEventListener("scroll", activeElementOnScroll);

/**
 * SCROLL REVEAL
 */

const revealElements = document.querySelectorAll("[data-reveal]");

const revealElementOnScroll = function () {
  for (let i = 0, len = revealElements.length; i < len; i++) {
    if (revealElements[i].getBoundingClientRect().top < window.innerHeight / 1.15) {
      revealElements[i].classList.add("revealed");
    } else {
      revealElements[i].classList.remove("revealed");
    }
  }
}

window.addEventListener("scroll", revealElementOnScroll);

window.addEventListener("load", revealElementOnScroll);

/**
 * APPOINTMENT MODAL
 * 
 * show the appointment modal when click "conseguir una cita" button
 */

const appointmentBtn = document.querySelector("[data-appointment-btn]");
const appointmentModal = document.querySelector("#appointmentModal");
const closeModalBtns = document.querySelectorAll("[data-close-modal]");

const openAppointmentModal = function () {
  appointmentModal.style.display = "flex";
  appointmentModal.style.justifyContent = "center";
  appointmentModal.style.alignItems = "center";
  appointmentModal.style.position = "fixed";
  appointmentModal.style.top = "50%";
  appointmentModal.style.left = "50%";
  appointmentModal.style.transform = "translate(-50%, -50%)";
  appointmentModal.style.backgroundColor = "var(--modal-background)";
  appointmentModal.style.color = "var(--modal-text)";
  appointmentModal.style.padding = "40px"; // Increased padding to make the box larger
  appointmentModal.style.boxShadow = "var(--shadow-2)";
  document.body.style.overflow = "hidden"; // Prevent scrolling
}

const closeAppointmentModal = function () {
  appointmentModal.style.display = "none";
  document.body.style.overflow = "auto"; // Restore scrolling
}

if (appointmentBtn) {
  appointmentBtn.addEventListener("click", openAppointmentModal);
}

if (closeModalBtns) {
  closeModalBtns.forEach(btn => {
    btn.addEventListener("click", closeAppointmentModal);
  });
}

window.addEventListener("click", function(event) {
  if (event.target == appointmentModal) {
    closeAppointmentModal();
  }
});
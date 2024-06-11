function toggleMenu() {
  var menu = document.querySelector('.menu');
  var iconContainer = document.querySelector('.icon-container');
  var hamburgerIcon = document.querySelector('.hamburger-icon');
  var closeIcon = document.querySelector('.close-icon');

  menu.classList.toggle('active');
  iconContainer.classList.toggle('show-close-icon');

  // Toggle visibility of hamburger and close icons
  hamburgerIcon.classList.toggle('hidden');
  closeIcon.classList.toggle('hidden');
}

function toggleAccordion(header) {
  var accordionItem = header;
  var arrow = accordionItem.querySelector('.arrow');
  var submenu = accordionItem.querySelector('ul');

  accordionItem.classList.toggle('active');
  arrow.classList.toggle('rotate');
  submenu.classList.toggle('active');
}

var iconContainer = document.querySelector('.icon-container');
var submenuItems = document.querySelectorAll('.menu-content li');

iconContainer.addEventListener('click', function(event) {
  event.stopPropagation();
  toggleMenu();
});

submenuItems.forEach(function(item) {
  item.addEventListener('click', function(event) {
    event.preventDefault(); // Prevent default link behavior
  });
});

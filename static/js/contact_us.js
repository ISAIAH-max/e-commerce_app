// Helper function to check if an element is in the viewport
function isElementInViewport(element) {
  var rect = element.getBoundingClientRect();
  return (
    rect.top >= 0 &&
    rect.left >= 0 &&
    rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
    rect.right <= (window.innerWidth || document.documentElement.clientWidth)
  );
}

// Handler function to add animation class when element is in viewport
function handleScroll() {
  var elements = document.querySelectorAll('.hidden');
  for (var i = 0; i < elements.length; i++) {
    if (isElementInViewport(elements[i])) {
      elements[i].classList.add('animated');
    }
  }
}

// Event listener for scroll event
window.addEventListener('scroll', handleScroll);

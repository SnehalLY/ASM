$.fn.commentCards = function() {
    return this.each(function() {
      var $this = $(this),
          $cards = $this.find('.card'),
          $current = $cards.filter('.card--current'),
          $next;
  
      // Function to switch cards
      function switchCard() {
        if (!$current.is(this)) {
          $cards.removeClass('card--current card--out card--next');
          $current.addClass('card--out');
          $current = $(this).addClass('card--current');
          $next = $current.next();
          $next = $next.length ? $next : $cards.first();
          $next.addClass('card--next');
        }
      }
  
      $cards.on('click', function() {
        if (!$current.is(this)) {
            // Switch to the clicked card if it's not the current one
            switchCard.call(this);
        } else {
            // Get the index of the clicked card
            var cardIndex = $(this).index();
            
            // Redirect to the corresponding Django URL
            var url = eventUrls[cardIndex]; 
            if (url) {
                window.location.href = url; // Redirect to the respective event page
            } else {
                console.log("No URL found for this card.");
            }
        }
    });
  
      // Automatic card switching at set intervals
      setInterval(function() {
        var $nextCard = $current.next().length ? $current.next() : $cards.first();
        switchCard.call($nextCard);
      }, 4000); // Set the interval (in milliseconds) to automatically switch cards
  
      // Initial setup to trigger the first card
      if (!$current.length) {
        $current = $cards.last();
        $cards.first().trigger('click');
      }
  
      $this.addClass('cards--active');
    });
};
  
// Initialize the commentCards function on the cards container
$('.cards').commentCards();  

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('studentForm');
  const popup = document.getElementById('popupMessage');
  const closeBtn = document.querySelector('.popup .close-btn');

  form.addEventListener('submit', (event) => {
      event.preventDefault(); // Prevent the default form submission
      
      // Show the popup
      popup.style.display = 'flex';
      
      // Optionally, you can reset the form after submission
      form.reset();
  });

  closeBtn.addEventListener('click', () => {
      popup.style.display = 'none';
  });

  // Close popup if user clicks outside of it
  window.addEventListener('click', (event) => {
      if (event.target === popup) {
          popup.style.display = 'none';
      }
  });
});

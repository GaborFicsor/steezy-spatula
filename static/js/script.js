$(document).ready(function() {
    $('.progress-bar').each(function() {
      var difficulty = parseInt($(this).attr('aria-valuenow'));
  
      if (difficulty == 20) {
        $(this).addClass('simple');
      } else if (difficulty == 40) {
        $(this).addClass('feasible');
      } else if (difficulty == 60) {
        $(this).addClass('engaging');
      } else {
        $(this).addClass('rewarding');
      }
    });
  });



// setTimeout(function() {
//     let messages = document.getElementById("alert");
//     let alert = new bootstrap.Alert(messages);
//     alert.close();
// }, 3000);


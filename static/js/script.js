// set progress-bar color based on recipe difficulty
// https://www.w3schools.com/jquery/misc_each.asp
// https://www.w3schools.com/jquery/html_addclass.asp

$(document).ready(function () {
  $('.progress-bar').each(function () {
    var difficulty = $(this).attr('aria-valuenow');

    if (difficulty == 20) {
      $(this).addClass('easy');
    } else if (difficulty == 40) {
      $(this).addClass('moderate');
    } else if (difficulty == 60) {
      $(this).addClass('intermediate');
    } else {
      $(this).addClass('challenging');
    }
  });
});

// hide alert messages after 3 seconds
// Code Institute's I think therefore I blog walkthrough project
$(document).ready(function () {
  setTimeout(function () {
    let messages = $('#alert');
    let alert = new bootstrap.Alert(messages);
    alert.close();
  }, 3000);
});

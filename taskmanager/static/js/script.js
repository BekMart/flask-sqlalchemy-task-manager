document.addEventListener('DOMContentLoaded', function() {
    // sidenav initialisation
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    //datepicker initialisation
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
      format: "dd mmmm, yyyy", // shows date as 01 Janurary, 2024
      i18n: {done: "Select"} // changes text on done button to select
    });

    // select initialisation
    let selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);
  });
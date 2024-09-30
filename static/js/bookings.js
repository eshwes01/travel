const editButtons = document.getElementsByClassName("btn-booking-edit");
const deleteButtons  = document.getElementsByClassName("btn-booking-delete");
const editBookingModal = new bootstrap.Modal(document.getElementById("editBookingModal"));
const deleteBookingModal = new bootstrap.Modal(document.getElementById("deleteBookingModal"))
const submitButton = document.getElementById("submitButton");
const editConfirm = document.getElementById("editConfirm");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
      let bookingId = e.target.getAttribute("data-booking_id");
      editConfirm.href = `edit_booking/${bookingId}`
      //let bookingMonth = e.target.getAttribut("");
      //booking.booking_month = 
      editBookingModal.show();
    });
  }

  for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let bookingId = e.target.getAttribute("data-booking_id");
      deleteConfirm.href = `delete_booking/${bookingId}`;
      deleteBookingModal.show();
    });
  }




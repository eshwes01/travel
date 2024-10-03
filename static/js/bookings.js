const deleteButtons  = document.getElementsByClassName("btn-booking-delete");
const deleteBookingModal = new bootstrap.Modal(document.getElementById("deleteBookingModal"));
const deleteConfirm = document.getElementById("deleteConfirm");

  for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let bookingId = e.target.getAttribute("data-booking_id");
      deleteConfirm.href = `delete_booking/${bookingId}`;
      deleteBookingModal.show();
    });
  }




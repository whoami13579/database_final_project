
document.addEventListener('DOMContentLoaded', function () {
    var myShowAllBtn = document.getElementById('show-all-btn')
    var myCloseAllBtn = document.getElementById('close-all-btn')

    if (myShowAllBtn != null) {
        myShowAllBtn.addEventListener('click', function () {
            $('.collapse').collapse('show')
        });
    }
    if (myCloseAllBtn != null) {
        myCloseAllBtn.addEventListener('click', function () {
            $('.collapse').collapse('hide')
        })
    }
});
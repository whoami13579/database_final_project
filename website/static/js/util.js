
document.addEventListener('DOMContentLoaded', function () {
    // Show all and Collapse all button
    var myShowAllBtn = document.getElementById('show-all-btn')
    var myCloseAllBtn = document.getElementById('close-all-btn')

    if (myShowAllBtn != null) {
        myShowAllBtn.addEventListener('click', function () {
            $('.collapse').collapse('show')
        })
    }
    if (myCloseAllBtn != null) {
        myCloseAllBtn.addEventListener('click', function () {
            $('.collapse').collapse('hide')
        })
    }

    var editPhotoBtn = document.getElementById('edit-photo-btn')
    if (editPhotoBtn != null) {
        editPhotoBtn.addEventListener('click', function() {
            var editPhotoDiv = document.getElementById('edit-photo')
            if (editPhotoDiv != null) {
                if (editPhotoDiv.style.display === 'none'){
                    editPhotoDiv.style.display = 'block'
                }
                else {
                    editPhotoDiv.style.display = 'none'
                }
            }
        })
    }
});
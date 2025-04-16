$(document).ready(function() {
    // Image preview
    $('#recipe-image-input').change(function() {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                $('#imagePreview').attr('src', e.target.result).removeClass('d-none');
                $('#uploadText').text('Change Image');
            }
            reader.readAsDataURL(file);
        }
    });

    // Form validation
    $('.needs-validation').submit(function(event) {
        if (!this.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();
        }
        $(this).addClass('was-validated');
    });
});

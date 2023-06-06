// create case stage
$(document).on('click', '.new-case-stage-link', function(e) {
    e.preventDefault();
    let title = "Register Case Stage";
    let url = $(this).data('href');
    let columnClass = "col-md-8";
    let containerFluid = true
    let formSelector = '.new-case-stage-form';

    ajaxPost(title, url, columnClass, containerFluid, formSelector)

});


// edit case stage
$(document).on('click', '.edit-case-stage-link', function(e) {
    e.preventDefault();
    let title = "Edit Case Stage";
    let url = $(this).data('href');
    let columnClass = "col-md-8";
    let containerFluid = true
    let formSelector = '.edit-case-stage-form';

    ajaxPost(title, url, columnClass, containerFluid, formSelector)
});


// delete case stage
$(document).on('click', '.delete-case-stage-link', function(e) {
    e.preventDefault();
    let title = "Delete Case Stage";
    let url = $(this).data('href');
    let content = "Are you sure you want to delete this case stage?";

    ajaxConfirm(title, url, content)
});
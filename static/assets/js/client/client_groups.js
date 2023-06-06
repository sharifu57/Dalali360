// create client group
$(document).on('click', '.new-client-group-link', function(e) {
    e.preventDefault();
    let url = $(this).data('href');
    let title = "New Client Group";
    let columnClass = "col-md-8";
    let containerFluid = true
    let formSelector = '.new-client-group-form';

    ajaxPost(title, url, columnClass, containerFluid, formSelector);

});


//edit client group
$(document).on('click', '.edit-client-group-link', function(e) {
    e.preventDefault();
    let url = $(this).data('href');
    let title = "Edit Client Group";
    let columnClass = "col-md-8";
    let containerFluid = true
    let formSelector = '.edit-client-group-form';

    ajaxPost(title, url, columnClass, containerFluid, formSelector);

});


//delete client group
$(document).on('click', '.delete-client-group-link', function(e) {
    e.preventDefault();
    let url = $(this).data('href');
    let title = "Delete Party Group";
    let content = "Are you sure you want to delete this party group?";

    ajaxConfirm(title, url, content);
});
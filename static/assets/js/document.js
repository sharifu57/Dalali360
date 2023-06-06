// create case document
$(document).on('click', '.new-document-link', function(e) {
    e.preventDefault();
    let title = "New Case Document";
    let url = $(this).data('href');
    let columnClass = "col-md-8";
    let containerFluid = true
    let formSelector = '.new-document-form';

    ajaxPost(title, url, columnClass, containerFluid, formSelector)

});


// edit case document
$(document).on('click', '.edit-case-document-link', function(e) {
    e.preventDefault();
    let title = "Edit Document";
    let url = $(this).data('href');
    let columnClass = "col-md-8";
    let containerFluid = true
    let formSelector = '.edit-document-form';

    ajaxPost(title, url, columnClass, containerFluid, formSelector)
});


// delete case document
$(document).on('click', '.delete-case-document-link', function(e) {
    e.preventDefault();
    let title = "Delete Document";
    let url = $(this).data('href');
    let content = "Are you sure you want to delete this record?";

    ajaxConfirm(title, url, content)
});
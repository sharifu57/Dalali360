//view court
$(document).on('click', '.view-court-link', function(e) {
    e.preventDefault();
    let title = false
    let url = $(this).data('href');
    let columnClass = "col-md-8";
    let containerFluid = true
    // let formSelector = '.new-court-form';

    ajaxGet(title, url, columnClass, containerFluid)
});

// create court
$(document).on('click', '.new-court-link', function(e) {
    e.preventDefault();
    let title = "Register Court";
    let url = $(this).data('href');
    let columnClass = "col-md-8";
    let containerFluid = true
    let formSelector = '.new-court-form';

    ajaxPost(title, url, columnClass, containerFluid, formSelector)
});


// edit court
$(document).on('click', '.edit-court-link', function(e) {
    e.preventDefault();
    let title = "Edit Court";
    let url = $(this).data('href');
    let columnClass = "col-md-8";
    let containerFluid = true
    let formSelector = '.edit-court-form';

    ajaxPost(title, url, columnClass, containerFluid, formSelector)

});


// delete court
$(document).on('click', '.delete-court-link', function(e) {
    e.preventDefault();
    let title = "Delete Court"
    let url = $(this).data('href');
    let content = "Are you sure you want to delete this court?"

    ajaxConfirm(title, url, content)

});



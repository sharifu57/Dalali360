// create client category
$(document).on("click", ".new-client-category-link", function (e) {
    let url = $(this).data('href');
    let title = "New Party Category";
    let columnClass = "col-md-8";
    let containerFluid = false
    let formSelector = '.new-client-category-form';

    ajaxPost(title, url, columnClass, containerFluid, formSelector);
});


//edit client category
$(document).on("click", ".edit-client-category-link", function (e) {
    let url = $(this).data('href');
    let title = "Edit Party Category";
    let columnClass = "col-md-8";
    let containerFluid = false
    let formSelector = '.edit-client-category-form';

    ajaxPost(title, url, columnClass, containerFluid, formSelector);
});

//delete Party category
$(document).on("click", ".delete-client-category-link", function(e) {
    let url = $(this).data('href');
    let title = "Delete Party Category";
    let content = "Are you sure you want to delete this Party category?";

    ajaxConfirm(title, url, content);
});
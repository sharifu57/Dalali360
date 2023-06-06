// create court category
$(document).on("click", ".new-court-category-link", function (e) {
    e.preventDefault();
    let title = "Register Court Category";
    let url = $(this).data('href');
    let columnClass = "col-md-8";
    let containerFluid = true;
    let formSelector = ".new-court-category-form";

    ajaxPost(title, url, columnClass, containerFluid, formSelector);
});


// edit court category
$(document).on("click", ".edit-court-category-link", function (e) {
    e.preventDefault();
    let title = "Edit Court Category";
    let url = $(this).data('href');
    let columnClass = "col-md-8";
    let containerFluid = true;
    let formSelector = ".edit-court-category-form";

    ajaxPost(title, url, columnClass, containerFluid, formSelector);
});


// delete court category
$(document).on("click", ".delete-court-category-link", function (e) {
    e.preventDefault();
    let title = "Delete Court Category";
    let url = $(this).data('href');
    let content = "Are you sure you want to delete this court category?";
    
    ajaxConfirm(title, url, content);
});
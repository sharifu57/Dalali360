$(document).on("click", ".new-case-category-link", function (e) {
    e.preventDefault();
    let title = "Register Case Category";
    let url = $(this).data('href');
    let columnClass = "col-md-8";
    let containerFluid = true;
    let formSelector = ".new-case-category-form";

    ajaxPost(title, url, columnClass, containerFluid, formSelector);
})


// delete case category
$(document).on("click", ".delete-case-category-link", function (e) {
    e.preventDefault();
    let title = "Delete Case Category";
    let url = $(this).data('href');
    let content = "Are you sure you want to delete this case category?";

    ajaxConfirm(title, url, content);
})


// edit case category
$(document).on("click", ".edit-case-category-link", function (e) {
    e.preventDefault();
    let title = "Edit Case Category";
    let url = $(this).data('href');
    let columnClass = "col-md-8";
    let containerFluid = true;
    let formSelector = ".edit-case-category-form";

    ajaxPost(title, url, columnClass, containerFluid, formSelector);
})

// show case category
$(document).on("click", ".show-case-category-link", function (e) {
    e.preventDefault();
    let title = "Show Case Category";
    let url = $(this).data('href');
    let columnClass = "col-md-8";
    let containerFluid = true;
    let formSelector = ".show-case-category-form";

    ajaxPost(title, url, columnClass, containerFluid, formSelector);
})
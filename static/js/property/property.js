$(document).on("click", ".add-new-propery-link", function(e) {
    let url = $(this).data('href');
    let title = "Add New Property";
    let columnClass = "col-md-8";
    let containerFluid = true
    let formSelector = ".new-property-form";
    let buttonsColumnClass = "";

    ajaxPost(title, url, columnClass, containerFluid, formSelector, buttonsColumnClass);
});
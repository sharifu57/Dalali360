// create client
$(document).on("click", ".new-client-link", function (e){
    e.preventDefault();
    let url = $(this).data('href');
    let title = "Create Party";
    let columnClass = "col-md-9";
    let containerFluid = false;
    let formSelector = ".new-client-form";

    ajaxPost(title, url, columnClass, containerFluid, formSelector);
});


// edit client
$(document).on("click", ".edit-client-link", function (e){
    e.preventDefault();
    let url = $(this).data('href');
    let title = "Edit Party";
    let columnClass = "col-md-9";
    let containerFluid = false;
    let formSelector = ".edit-client-form";

    ajaxPost(title, url, columnClass, containerFluid, formSelector);
});


//delete client 
$(document).on("click", ".delete-client-link", function (e){
    e.preventDefault();
    let url = $(this).data('href');
    let title = "Delete Party";
    let content = "Are you sure you want to delete this Party?";

    ajaxConfirm(title, url, content);
});


//show client
$(document).on("click", ".show-client-link", function (e){
    e.preventDefault();
    let url = $(this).data('href');
    let title = "Party Details";
    let columnClass = "col-md-8"
    let containerFluid = true

    ajaxGet(title, url, columnClass, containerFluid);
});

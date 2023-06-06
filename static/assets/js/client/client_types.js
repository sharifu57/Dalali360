// create client type
$(document).on("click", ".new-client-type-link", function(e) {
    e.preventDefault();
   let url = $(this).data('href');
   let title = "New Party Type";
   let columnClass = "col-md-8";
   let containerFluid = false
   let formSelector = '.new-client-type-form';

   ajaxPost(title, url, columnClass, containerFluid, formSelector);
});


//edit client type
$(document).on("click", ".edit-client-type-link", function(e) {
    e.preventDefault();
   let url = $(this).data('href');
   let title = "Edit Party Type";
   let columnClass = "col-md-8";
   let containerFluid = false
   let formSelector = '.edit-client-type-form';

   ajaxPost(title, url, columnClass, containerFluid, formSelector);
});


//delete client type
$(document).on("click", ".delete-client-type-link", function(e) {
    e.preventDefault();
   let url = $(this).data('href');
   let title = "Delete Party Type";
   let content = "Are you sure you want to delete this Party type?";

   ajaxConfirm(title, url, content);
});
// Register new case
$(document).on("click", ".add-new-propery-link", function(e) {
    let url = $(this).data('href');
    let title = "Add New Property";
    let columnClass = "col-md-8";
    let containerFluid = true
    let formSelector = ".new-prorperty-form";
    let buttonsColumnClass = "";

    ajaxPost(title, url, columnClass, containerFluid, formSelector, buttonsColumnClass);
});


// Edit case
$(document).on("click", ".edit-case-link", function(e) {
    let url = $(this).data('href');
    let title = "Edit Case";
    let columnClass = "col-md-8";
    let containerFluid = true
    let formSelector = ".edit-case-form";
    let buttonsColumnClass = "";

    ajaxPost(title, url, columnClass, containerFluid, formSelector, buttonsColumnClass);
});


//Add date of appearance
$(document).on("click", ".add-date-of-appearance-link", function(e) {
    let url = $(this).data('href');
    let title = "Add Date of Appearance";
    let columnClass = "col-md-8";
    let containerFluid = true
    let formSelector = ".add-date-of-appearance-form";
    let buttonsColumnClass = "";

    ajaxPost(title, url, columnClass, containerFluid, formSelector, buttonsColumnClass);
});

// Show date of appearance
$(document).on("click", ".show-date-of-appearance-link", function(e) {
    let url = $(this).data('href');
    let title = "Date of Appearance";
    let columnClass = "col-md-12";
    let containerFluid = true

    ajaxGet(title, url, columnClass, containerFluid);
});


// Delete date of appearance
$(document).on("click", ".delete-date-of-appearance-link", function(e) {
    let url = $(this).data('href');
    let title = "Delete Date of Appearance";
    let content = "Are you sure you want to delete this date of appearance?";

    ajaxConfirm(title, url, content);
});


// Edit date of appearance
$(document).on("click", ".edit-date-of-appearance-link", function(e) {
    let url = $(this).data('href');
    let title = "Edit Date of Appearance";
    let columnClass = "col-md-8";
    let containerFluid = true
    let formSelector = ".edit-date-of-appearance-form";
    let buttonsColumnClass = "";

    ajaxPost(title, url, columnClass, containerFluid, formSelector, buttonsColumnClass);
});



// create new case nature
$(document).on('click', '.new-case-nature-link', function(e) {
    e.preventDefault();
    let title = "New Case Nature";
    let url = $(this).data('href');
    let columnClass = "col-md-8";
    let containerFluid = true
    let formSelector = '.new-case-nature-form';

    ajaxPost(title, url, columnClass, containerFluid, formSelector)

});


// edit case nature
$(document).on('click', '.edit-case-nature-link', function(e) {
    e.preventDefault();
    let title = "Edit Case Nature";
    let url = $(this).data('href');
    let columnClass = "col-md-8";
    let containerFluid = true
    let formSelector = '.edi-case-nature-form';

    ajaxPost(title, url, columnClass, containerFluid, formSelector)
});


// delete case nature
$(document).on('click', '.delete-case-nature-link', function(e) {
    e.preventDefault();
    let title = "Delete Case Nature";
    let url = $(this).data('href');
    let content = "Are you sure you want to delete this record?";

    ajaxConfirm(title, url, content)
});

// activate case nature
$(document).on('click', '.activate-case-nature-link', function(e) {
    console.log('activate case nature')
    e.preventDefault();
    let title = "Activate Case Nature";
    let url = $(this).data('href');
    let content = "Are you sure you want to Activate this case nature?";

    ajaxConfirm(title, url, content)
});





// Add case date of submission
$(document).on('click', '.add-case-date-of-submission-link', function(e) {
    console.log('clicked');
    e.preventDefault();
    let title = "Add Case Date of Submission";
    let url = $(this).data('href');
    let columnClass = "col-md-8";
    let containerFluid = true
    let formSelector = '.add-case-date-of-submission-form';

    ajaxPost(title, url, columnClass, containerFluid, formSelector)
});


// Add case event types
$(document).on('click', '.add-case-event-types-link', function(e) {
    e.preventDefault();
    let title = "Add Case Event Type";
    let url = $(this).data('href');
    let columnClass = "col-md-8";
    let containerFluid = true
    let formSelector = '.add-case-event-types-form';

    ajaxPost(title, url, columnClass, containerFluid, formSelector);
});


// edit case event types
$(document).on('click', '.edit-case-event-types-link', function(e) {
    e.preventDefault();
    let title = "Edit Case Event Type";
    let url = $(this).data('href');
    let columnClass = "col-md-8";
    let containerFluid = true
    let formSelector = '.edit-case-event-types-form';
    ajaxPost(title, url, columnClass, containerFluid, formSelector);
});


// delete case event types
$(document).on('click', '.delete-case-event-types-link', function(e) {
    e.preventDefault();
    let title = "Delete Case Event Type";
    let url = $(this).data('href');
    let content = "Are you sure you want to delete this record?";
    ajaxConfirm(title, url, content);
});

// Assign case to advocate
$(document).on('click', '.assign-case-to-advocate-link', function(e) {
    e.preventDefault();
    let title = "Assign Case to Advocate";
    let url = $(this).data('href');
    let columnClass = "col-md-8";
    let containerFluid = true
    let formSelector = '.assign-case-to-advocate-form';

    ajaxPost(title, url, columnClass, containerFluid, formSelector)
});

// settle case
$(document).on('click', '.settle-case-link', function(e) {
    e.preventDefault();
    let title = "Settle Case";
    let url = $(this).data('href');
    let columnClass = "col-md-8";
    let containerFluid = true
    let formSelector = '.settle-case-form';

    ajaxPost(title, url, columnClass, containerFluid, formSelector)
});


// close case
$(document).on('click', '.close-case-link', function(e) {
    e.preventDefault();
    let title = "Close Case";
    let url = $(this).data('href');
    let columnClass = "col-md-8";
    let containerFluid = true
    let formSelector = '.close-case-form';

    ajaxPost(title, url, columnClass, containerFluid, formSelector)
});


// edit case date of submission
$(document).on('click', '.edit-case-date-of-submission-link', function(e) {
    e.preventDefault();
    let title = "Edit Case Date of Submission";
    let url = $(this).data('href');
    let columnClass = "col-md-8";
    let containerFluid = true
    let formSelector = '.edit-case-date-of-submission-form';

    ajaxPost(title, url, columnClass, containerFluid, formSelector)
});


//delete case date of submission
$(document).on('click', '.delete-case-date-of-submission-link', function(e) {
    e.preventDefault();
    let title = "Delete Case Date of Submission";
    let url = $(this).data('href');
    let content = "Are you sure you want to delete this record?";

    ajaxConfirm(title, url, content)
});



//mark case final
$(document).on('click', '.mark-case-final-link', function(e) {
    e.preventDefault();
    let title = "Mark Case Final";
    let url = $(this).data('href');
    let content = "Are you sure you want to mark this case as final?, You wont be able to access it again";

    ajaxConfirm(title, url, content)
});


$(document).ready(
    function(){ var fileTarget = $('.image-section .image-input'); fileTarget.on('change', function(){
    if(window.FileReader){ 
        var filename = $(this)[0].files[0].name; 
    } else { 
        var filename = $(this).val().split('/').pop().split('\\').pop(); 
    } 
    
    $(this).siblings('.upload-name').val(filename);
     }); 
    });

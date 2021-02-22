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


var textTarget1 = document.querySelector('.image-section').lastElementChild.previousSibling;
textTarget1.textContent="";

var textTarget2 = textTarget1.previousSibling.previousSibling.previousSibling;
textTarget2.textContent="기존";
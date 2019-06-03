$(document).ready(function ()
    {
    	$('.option').click(function(event){
    		//  Hacer que el header 
    		$(this).parent()
    				.find(".criterion-header").addClass("w3-red");
    		$(this).parent()
    				.find(".criterion-header").removeClass("w3-orange");
            $(this).parent()
                    .find(".not-selected-warning")
                    .html('<i class="far fa-check-circle"></i>');

    		$(this).parent()
                    .children().removeClass("selected");

            $(this).find("input").prop("checked", true);
            $(this).addClass("selected");
    	});
    });

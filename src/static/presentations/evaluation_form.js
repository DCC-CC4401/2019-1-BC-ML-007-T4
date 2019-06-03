$(document).ready(function ()
    {
    	$('.option').click(function(event){
    		//  Hacer que el header 
    		$(this).parent()
    				.find(".criterion-header").toggleClass("w3-red");
    		$(this).parent()
    				.find(".criterion-header").removeClass("w3-orange");
    		$(this).addClass("selected");
    	});
    };

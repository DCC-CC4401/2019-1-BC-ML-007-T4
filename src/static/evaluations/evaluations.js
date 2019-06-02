"use strict";

function myFunction(id)
{
    var x = document.getElementById(id);
    if (x.className.indexOf("w3-show") == -1)
    {
        x.className += " w3-show";
    }
    else
    {
        x.className = x.className.replace(" w3-show", "");
    }
}

// No hacerle prettify plspls
$(document).ready(function ()
    {
    	$('.criterion-option').click(function(event){
    		//  Hacer que el header 
    		$(this).parent()
    				.find(".criterion-header").toggleClass("w3-red");
    		$(this).parent()
    				.find(".criterion-header").removeClass("w3-orange");
    		$(this).addClass("selected");
    	});
    };

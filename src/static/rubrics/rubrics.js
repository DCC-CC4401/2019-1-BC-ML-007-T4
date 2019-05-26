"use strict";

function myFunction( id )
{
    var x = document.getElementById( id );
    if ( x.className.indexOf( "w3-show" ) == -1 )
    {
        x.className += " w3-show";
    }
    else
    {
        x.className = x.className.replace( " w3-show", "" );
    }
}

$(document).ready(
    function()
    {
        $( ".rubric_table" ).addClass("w3-table-all");
        $( ".rubric_table thead" ).addClass("w3-light-grey");
    }
)

"use strict";

function detailToggle( id )
{
    $( `#${id}` ).toggleClass("w3-show");
}

$(
    function()
    {
        $( ".rubric_table" ).addClass("w3-table-all");
        $( ".rubric_table thead" ).addClass("w3-light-grey");
    }
)

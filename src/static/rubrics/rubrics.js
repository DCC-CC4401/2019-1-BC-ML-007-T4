"use strict";

function detailToggle( id )
{
    $( `#${id}` )
        .toggleClass( "w3-show" );
}

function deleteDialogToggle( dialog_id )
{
    $( `#${dialog_id}` )
        .css( "display", ( index, current_value ) =>
        {
            return current_value === "none" ? "block" : "none";
        } );
}

$(
    function ()
    {
        $( ".rubric_table" )
            .addClass( "w3-table-all" );
        $( ".rubric_table thead" )
            .addClass( "w3-light-grey" );
    }
)
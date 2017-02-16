/**
 * Exercise #8: Card board
 */

$(document).ready(function() {

    // This is for you to complete

    var sizeCols = 3;
    var sizeRows = 4;

    for (var row = 0; row < sizeRows; row++) {
        for (var col = 0; col < sizeCols; col++) {
            var card = $("<div></div>").addClass("card");
            if (col == 0) {
                card.addClass("clearleft");
            }
            $("#cardboard").append(card);
        }
    }

});
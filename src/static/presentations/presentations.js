//enable csrf post ajax
// Function taken from: https://stackoverflow.com/a/4004010/10216044

if (typeof String.prototype.trimLeft !== "function") {
        String.prototype.trimLeft = function() {
            return this.replace(/^\s+/, "");
        };
}

if (typeof String.prototype.trimRight !== "function") {
        String.prototype.trimRight = function() {
                return this.replace(/\s+$/, "");
        };
}

if (typeof Array.prototype.map !== "function") {
        Array.prototype.map = function(callback, thisArg) {
                for (var i=0, n=this.length, a=[]; i<n; i++) {
                        if (i in this) a[i] = callback.call(thisArg, this[i]);
                }
                return a;
        };
}

function getCookies() {
        var c = document.cookie, v = 0, cookies = {};
        if (document.cookie.match(/^\s*\$Version=(?:"1"|1);\s*(.*)/)) {
                c = RegExp.$1;
                v = 1;
        }
        if (v === 0) {
                c.split(/[,;]/).map(function(cookie) {
                var parts = cookie.split(/=/, 2),
                        name = decodeURIComponent(parts[0].trimLeft()),
                        value = parts.length > 1 ? decodeURIComponent(parts[1].trimRight()) : null;
                cookies[name] = value;
                });
        } else {
                c.match(/(?:^|\s+)([!#$%&'*+\-.0-9A-Z^`a-z|~]+)=([!#$%&'*+\-.0-9A-Z^`a-z|~]*|"(?:[\x20-\x7E\x80\xFF]|\\[\x00-\x7F])*")(?=\s*[,;]|$)/g).map(function($0, $1) {
                var name = $0,
                        value = $1.charAt(0) === '"'
                                ? $1.substr(1, -1).replace(/\\(.)/g, "$1")
                                : $1;
                cookies[name] = value;
                });
        }
        return cookies;
}

function getCookie(name) {
        return getCookies()[name];
}

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
            }
        );

        const current_url = $(location).attr('href')
        const current_split_url = current_url.split('/')

        const evaluation_id = current_split_url[current_split_url.length-2];
        const group_id = current_split_url[current_split_url.length-1];

        function update_with_context(context)
        {
                //console.log(context)
        }
        
        setInterval(() =>
        {
                $.ajax({
                        type: "POST",
                        url: current_url+"/update_context",
                        data: {},
                        headers: {"X-CSRFToken": getCookie("csrftoken")},
                        success: function (response) {
                                update_with_context(response);
                        }
                });
        }, 5000);

        // Agregar js para avisar que la duración no está en el intervalo
        $("#duration-input").keyup(function(event){
            var min = parseFloat($("#duration-min").html(),10);
            var max = parseFloat($("#duration-max").html(),10);
            var time = parseFloat($("#duration-input").val(),10);
            console.log(min<time)
            if(!(min <= time && time <= max))
                $("#discount-warning").html("Se debe descontar por duración.");
            else
                $("#discount-warning").html("");
        })
    });

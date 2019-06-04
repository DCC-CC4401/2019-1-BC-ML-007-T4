//enable csrf post ajax
// Function taken from: https://stackoverflow.com/a/4004010/10216044

Array.prototype.diff = function(a) {
        return this.filter(function(i) {return a.indexOf(i) < 0;});
};

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

let old_context;

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

        $('.add_evaluator_trigger').click(function(event){
                $("#add_evaluator_modal").show();
                }
        );

        $('.add_presentator_trigger').click(function(event){
                $("#add_presentator_modal").show();
                }
        );

        old_context = {
                "allowed_evaluators": [],
                "current_presentators": [],
                "evaluation_status": $("#status_message").hasClass("done") ? true : false,
                "group_members": [],
        };

        $("#evaluators_list .evaluator_item").each(
                (idx, li) => {
                        let evaluator_name = $(li).children(".evaluator_name").text().replace(/\n/gm, "").trimLeft().trimRight();
                        let evaluator_status_element = $(li).children(".evaluator_status")
                        let evaluator_status = evaluator_status_element.hasClass("done") ? "done" : evaluator_status_element.hasClass("evaluating") ? "evaluating" : "pending";
                        old_context["allowed_evaluators"].push([evaluator_name, evaluator_status]);
                }
        );

        $("#presentators_list .presentator_item").each(
                (idx, li) => {
                        let presentator_name = $(li).children(".presentator_name").text().replace(/\n/gm, "").trimLeft().trimRight();
                        old_context["current_presentators"].push(presentator_name);
                }
        );

        $("#group_member_list .group_member_item").each(
                (idx, li) => {
                        let group_member_name = $(li).children(".group_member_name").text().replace(/\n/gm, "").trimLeft().trimRight();
                        let group_member_status_element = $(li).children(".group_member_status")
                        let group_member_status = group_member_status_element.hasClass("done") ? "done" : "pending";
                        old_context["group_members"].push([group_member_name, group_member_status]);
                }
        );

        const current_url = $(location).attr('href')
        const current_split_url = current_url.split('/')

        const evaluation_id = current_split_url[current_split_url.length-2];
        const group_id = current_split_url[current_split_url.length-1];

        function update_with_context(context)
        {
                for (element in old_context.allowed_evaluators)
                {
                        let evaluator = element[0];
                        let status = element[1];
                        let exists = false;
                        for (new_element in context.allowed_evaluators)
                        {
                                let new_evaluator = new_element[0];
                                let new_status = new_element[1];
                                if (evaluator == new_evaluator && status != new_status)
                                {
                                        exists = true;

                                        let status_span = $(`#${evaluator}`).children("span.evaluator_status").removeClass(status).addClass(new_status);

                                        status_span.children().detach();

                                        switch (new_status) {
                                                case "done":
                                                        status_span.append(`<i style="margin-left: 10px" class="presentado far fa-check-circle"></i>
                                                        <i class="presentado w3-small">
                                                          ya evaluó
                                                        </i>`);
                                                        break;
                                                case "evaluating":
                                                        status_span.append(`<i style="margin-left: 10px" class="fa fa-spinner fa-lg fa-spin"></i>
                                                        <i class="w3-small">
                                                          evaluando
                                                        </i>`);
                                                        break;
                                                default:
                                                        status_span.append(`<i style="margin-left: 10px" class="w3-large fas fa-times"></i>
                                                        <i class="w3-small">
                                                          aún no evalúa
                                                        </i>`);
                                                        break;
                                        }
                                }
                        }

                        if (!exists)
                        {
                                $(`#${evaluator}`).detach();
                        }
                }

                for (new_element in context.allowed_evaluators)
                {
                        let new_evaluator = new_element[0];
                        let new_status = new_element[1];

                        let exists = false;
                        for (element in old_context.allowed_evaluators)
                        {
                                let evaluator = element[0];
                                let status = element[1];
                                if (new_evaluator == evaluator)
                                {
                                        exists = true;
                                }
                        }

                        if (!exists)
                        {
                                let status_text = "";

                                if (new_status == "done")
                                {
                                        status_text = `<i style="margin-left: 10px" class="presentado far fa-check-circle"></i>
                                        <i class="presentado w3-small">
                                          ya evaluó
                                        </i>`;
                                }
                                else if (new_status == "evaluating") {
                                        status_text = `<i style="margin-left: 10px" class="fa fa-spinner fa-lg fa-spin"></i>
                                        <i class="w3-small">
                                          evaluando
                                        </i>`;
                                }
                                else
                                {
                                        status_text = `<i style="margin-left: 10px" class="w3-large fas fa-times"></i>
                                        <i class="w3-small">
                                          aún no evalúa
                                        </i>`;
                                }

                                $("#evaluator_list").append(`<li id="${new_evaluator}" class="evaluator_item w3-padding-16">
                                        <span class="evaluator_name">
                                                ${new_evaluator}
                                        </span>
                                        <span class="evaluator_status ${new_status}">
                                                ${status_text}
                                        </span>
                                </li>`);
                        }
                }
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

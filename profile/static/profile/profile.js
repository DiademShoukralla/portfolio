window.onload = function() {
    var cancelbtns = document.getElementsByClassName('cancel');
    var togglebtns = document.getElementsByClassName('toggle');
    var submitbtns = document.getElementsByClassName('submit');

    // Same number of buttons
    for (var i = 0; i < cancelbtns.length; i++){
        cancelbtns[i].innerHTML = "&#10006";
        cancelbtns[i].title = "cancel";
        togglebtns[i].innerHTML = "&#9998";
        togglebtns[i].title = "edit";
        submitbtns[i].innerHTML = "&#10003";
        submitbtns[i].title = "submit";
    }

};

function btnToggle(elmnt){
    startEditDisplay(elmnt);
}


function btnCancel(elmnt){
    endEditDisplay(elmnt);
    var box = elmnt.parentElement.getElementsByClassName('input-text')[0];
    box.value = box.getAttribute('value');
}


function btnSubmit(elmnt){
    endEditDisplay(elmnt);
    var box = elmnt.parentElement.getElementsByClassName('input-text')[0];
    var name = box.name;
    var values = {};
    values[name] = box.value;
    $.ajax({
        url: '/profile/update/',
        method: 'POST',
        beforeSend: function(request) {
            request.setRequestHeader("X-CSRFToken", $.cookie("csrftoken"));
        },
        data: values,
        dataType: 'text',
        success: function setTextBox(data){
            box.value = data;
        }
      });
}


// Helper functions
function startEditDisplay(elmnt){
    togglebtn = elmnt.parentElement.getElementsByClassName('toggle')[0];
    cancelbtn = elmnt.parentElement.getElementsByClassName('cancel')[0];
    submitbtn = elmnt.parentElement.getElementsByClassName('submit')[0];
    input = elmnt.parentElement.getElementsByClassName('input-text')[0];
    togglebtn.style.display = 'none';
    cancelbtn.style.display = 'block';
    submitbtn.style.display = 'block';
    input.disabled = false;
    input.focus();
    input.setSelectionRange(0, input.value.length * 2);
}


function endEditDisplay(elmnt){
    togglebtn = elmnt.parentElement.getElementsByClassName('toggle')[0];
    cancelbtn = elmnt.parentElement.getElementsByClassName('cancel')[0];
    submitbtn = elmnt.parentElement.getElementsByClassName('submit')[0];
    input = elmnt.parentElement.getElementsByClassName('input-text')[0];
    togglebtn.style.display = 'block';
    cancelbtn.style.display = 'none';
    submitbtn.style.display = 'none';
    input.disabled = true;
}


function upload(elmnt){
    var form = elmnt.parentElement;
    form.submit();
     $.ajax({
        url: '/profile/update/',
        method: 'POST',
        beforeSend: function(request) {
            request.setRequestHeader("X-CSRFToken", $.cookie("csrftoken"));
        },
        data: values,
        dataType: 'text',
        success: function setTextBox(data){
            box.value = data;
        }
      });
}

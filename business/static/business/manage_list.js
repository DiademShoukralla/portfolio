function create(){
    shadow.style.display = 'block';
    float.style.display = 'block';
}

function cancel(){
    shadow.style.display = 'none';
    float.style.display = 'none';
}

function submit(){
    var form = document.getElementsByClassName('create-input');
    var values = {};
    for(var i=0; i<form.length; i++){
        values[form[i].name] = form[i].value
    }
    $.ajax({
        url: '/business/manage/create/',
        method: 'POST',
        beforeSend: function(request) {
            request.setRequestHeader("X-CSRFToken", $.cookie("csrftoken"));
        },
        data: values,
        dataType: 'text',
        success: function reload(data){
            location.reload();
        }
      });

}

window.onload = function (e){
    shadow = document.getElementById('shadow')
    float = document.getElementById('float')

}

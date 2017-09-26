function preview() {

    var preview = document.querySelector('img');
    var file = document.querySelector('input[type=file]').files[0];
    var reader = new FileReader();
    reader.onloadend = function() {
        preview.src = reader.result;
    };


    if (file) {
        reader.readAsDataURL(file);
    }
    console.log(preview);
}


function getCookie(name) {
          var cookieValue = null;
          if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
          for (var i = 0; i < cookies.length; i++) {
               var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) == (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
             }
          }
      }
 return cookieValue;
}


$('#canvasDiv').mouseup(function (e) {
    e.preventDefault();
    var csrftoken = getCookie('csrftoken');


    var canvas = document.getElementById('canvasDiv');
    var context = canvas.getContext('2d');
    console.log(context);

    var dataurl = canvas.toDataURL('image/jpg');

    var data = new FormData();

    data.append('edge', document.getElementById('demo2').getAttribute('src'));
    data.append('color', dataurl);
    data.append('csrfmiddlewaretoken', csrftoken);

    $.ajax({
        url: 'Color/',
        type: 'POST',
        data: data,
        processData: false,
        contentType: false,
    success : function(data) {
       $('#temp').attr('src', data['color'])
    },
    error : function () {
        console.log('Something is going wrong.');
    }
    })

});


$('#main_image').change(function (e) {
    e.preventDefault();
    var csrftoken = getCookie('csrftoken');

    var files = document.getElementById('main_image').files;
    var formData = new FormData();

    for(var i = 0; i < files.length; i++){
        var file = files[i];
        formData.append('image', file, file.name);
    }

    formData.append('csrfmiddlewaretoken', csrftoken);
    $.ajax({
        url: 'Savings/',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
    success : function(result){
        $('#demo2').attr('src', 'data:image/png;base64,' + result['image']);
        console.log('Image was uploaded. Pk: ' + result['id']);
        var canvas = document.getElementById('canvasDiv');
        canvas.setAttribute('width', 512);
        canvas.setAttribute('height', 512);
        var context = canvas.getContext('2d');
    },
    error : function(xhr, errmsgm, err) {
        console.log('Something wrong. Image was not uploaded.');
    }
    });
});
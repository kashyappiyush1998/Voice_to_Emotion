$(document).ready(function(){
    let file;
    const input = document.querySelector("input#input-voice");
    $("#input-voice").change( function(e) {
        var reader = new FileReader();
        reader.onload = function (e) {
          console.log(e.target.result)
        };
        reader.readAsDataURL(e.target.files[0]);
    })

    $("#get-emotion").click( function (e) {
        uploadImages(input.files[0])
    })

});

function uploadImages(file){
  var formData = new FormData();
  formData.append('file',file);

  $.ajax({
    url:'/upload-emotion',
    data:formData,
    type:'POST',
    cache:false,
    contentType:false,
    processData:false,
    // beforeSend: function() {
    //   document.querySelector(".btn-upload").innerText = "Uploading...";
    //   document.querySelector(".btn-upload").disabled = true;
    // },
    success:function(r){
      $("#emotion-text").text(r);
    },
    failure: function(e) {
      console.log(e)
    }
})
}
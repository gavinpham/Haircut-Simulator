function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#input_img')
            .attr('src', e.target.result)
            .width(150)
            .height(200);
        };

        reader.readAsDataURL(input.files[0]);
    }
}
/*
$("button").click(function(){

}

    )
$.ajax({
  type: "POST",
  url: "~/pythoncode.py",
  data: { param: text}
}).done(function( o ) {
   // do something
});
*/
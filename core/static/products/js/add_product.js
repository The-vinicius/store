var images = [];
function image_select() {
  images = [];
  var image = document.getElementById("id_image").files;
  for (i = 0; i < image.length; i++) {
      images.push({
        "name" : image[i].name,
        "url" : URL.createObjectURL(image[i]),
        "file" : image[i],
    });
  }
  document.getElementById("container").innerHTML = image_show()
}
function image_show() { 
    var image = "";
    images.forEach((i) => {
      image += '<div class="image_container d-flex justify-content-cener position-relative"><img src="'+ i.url +'" alt="Image"></div>'
          })
    return image;
}

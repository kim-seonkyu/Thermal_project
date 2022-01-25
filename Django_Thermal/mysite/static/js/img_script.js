var req = new XMLHttpRequest();
req.open("GET", "/static/json/image_list.json");
req.onreadystatechange = function(){
  if( this.readyState == 4){
    console.log(this.response);
    var data = JSON.parse(this.response)
    for( var i = 0; i < data.length; i++){
      var div = document.createElement("div");
      div.setAttribute("class", "images");
      div.onclick = function() {
        this.classList.toggle("images-selected")
      }
      
      var timerId;
      div.onmouseover = function(){
        var element = this;
        this.timerId = setTimeout(function(){
          element.classList.add("images-magnified");
        }, 1000 );
      }

      div.onmouseout = function(){
        clearTimeout(this.timerId);
        this.classList.remove("images-magnified");
      }

      var img = document.createElement("img");
      img.src = data[i];
      div.appendChild(img);
      document.body.appendChild(div);
    }
  }
}
req.send();
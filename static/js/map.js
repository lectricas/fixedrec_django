$(document).ready(function(){
    $('.list-group-item').on('click', function() {
        var $this = $(this);

        $('.active').removeClass('active');
        $this.toggleClass('active')

        // Pass clicked link element to another function
        create_request($this);
    });
});


function create_request ($this){
//    $("#loading").show();
      var uuid = $this.data('item');
//    var hasta = $("#hasta").val();
//    var tipo_edad = $("#tipo-edad").val();
//    var sexo = $("#sexo").val();
//    var fuerza = $("#fuerza").val();
//    var provincia = $("#provincia").val();
    $.get( "/locations/tracks/"+uuid, {
          format:"json",
//        tipo_edad: tipo_edad,
//        sexo: sexo,
//        fuerza: fuerza,
//        provincia: provincia
    }, function( data ) {
        try{
//            remueve_marcadores();
        }catch(err){
          //Handle errors here
        }
//        $("#loading").hide();
        create_polyline(data);
    });
}



function create_polyline(data){

    var points = data.points;
    var points_length = points.length;
    var coords = [];
    for (var i = 0; i < points_length; i++) {
        var lat = parseFloat(points[i].lat);
        var lng = parseFloat(points[i].lng);
        coords.push({lat: lat, lng: lng});
    }
    initMap(coords);

}


function initMap(coords) {


   if (typeof coords === "undefined") {
        var coords = [];
        coords.push({56.85297: 53.2167709, 56.85298: 53.2167710});
   }

  var bounds = new google.maps.LatLngBounds();
  for (var i = 0; i < coords.length; i++) {
      var point = coords[i];
      var latlng = new google.maps.LatLng(point.lat, point.lng);
      bounds.extend(latlng);

  }
  var map = new google.maps.Map(document.getElementById('map-canvas'), {
    zoom: 3,
    center: bounds.getCenter(),
    mapTypeId: google.maps.MapTypeId.TERRAIN
  });
  var flightPath = new google.maps.Polyline({
    path :coords,
    geodesic: true,
    strokeColor: '#FF0000',
    strokeOpacity: 1.0,
    strokeWeight: 2
  });


  flightPath.setMap(map);
  map.fitBounds(bounds);
}
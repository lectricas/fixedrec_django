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
        initMap(data);
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


function initMap(data) {



    var myOptions = {
        center: new google.maps.LatLng(45.4555729, 9.169236),
        zoom: 13,
        mapTypeId: google.maps.MapTypeId.ROADMAP};


    var coordinates = [];
    var bounds = new google.maps.LatLngBounds();
    var flightPath = new google.maps.Polyline()

    var map = new google.maps.Map(document.getElementById('map-canvas'), myOptions);

     if(typeof data != 'undefined'){

        var points = data.points;
        var points_length = points.length;


        for (var i = 0; i < points_length; i++) {
            var lat = parseFloat(points[i].lat);
            var lng = parseFloat(points[i].lng);
            var latlng = new google.maps.LatLng(lat, lng)
            coordinates.push(latlng);
            bounds.extend(latlng);


        }


        var start = coordinates[0];
        var finish = coordinates[coordinates.length-1]
        var marker = new google.maps.Marker({
            position: start,
            icon: 'http://maps.google.com/mapfiles/kml/paddle/grn-stars_maps.png',
            map: map,
        });

        var marker = new google.maps.Marker({
            position: finish,
            map: map,
            icon: 'http://maps.google.com/mapfiles/kml/paddle/pink-stars_maps.png',
        });

        flightPath = new google.maps.Polyline({
            path :coordinates,
            geodesic: true,
            strokeColor: '#FF0000',
            strokeOpacity: 1.0,
            strokeWeight: 2
            });

            flightPath.setMap(map);
            map.fitBounds(bounds);
    }




}





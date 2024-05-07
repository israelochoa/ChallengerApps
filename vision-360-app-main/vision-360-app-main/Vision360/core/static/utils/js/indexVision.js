
function initMap() {
  const map = new google.maps.Map(document.getElementById("seccion1"), {
    zoom: 5,

  });
  // Define the LatLng coordinates for the polygon's path.
 
  const triangleCoords = [
    { lat: -4.0305000, lng: -79.199924 },
    { lat: -4.031154,  lng: -79.198982 },
    { lat: -4.031877,  lng: -79.199282 },
    { lat: -4.035468, lng: -79.199704 }, // Corrected latitude from 4.035468 to -4.035468
    { lat: -4.037297, lng: -79.200305 },
    { lat: -4.036880, lng: -79.203009 },
    { lat: -4.038573, lng: -79.203672 },
    { lat: -4.036990, lng: -79.206077 },
    { lat: -4.030563, lng: -79.200026 },
  ];
  
  // Construct the polygon.
  const bermudaTriangle = new google.maps.Polygon({
    paths: triangleCoords,
    strokeColor: "#FF0000",
    strokeOpacity: 0.8,
    strokeWeight: 2,
    fillColor: "#FF0000",
    fillOpacity: 0.35,
  });

  bermudaTriangle.setMap(map);
}

window.initMap = initMap;
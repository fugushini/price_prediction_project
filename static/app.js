function getBuildingType() {
  var buildingTypes = document.getElementsByName("uiBuildingType");
  for (var i = 0; i < buildingTypes.length; i++) {
    if (buildingTypes[i].checked) {
      return parseInt(buildingTypes[i].value);
    }
  }
  return -1;
}

function getObjectType() {
  var objectTypes = document.getElementsByName("uiObType");
  for (var i = 0; i < objectTypes.length; i++) {
    if (objectTypes[i].checked) {
      return parseInt(objectTypes[i].value);
    }
  }
  return -1;
}

function onClickedEstimatePrice() {

  console.log("Estimate price button clicked");

  var area = document.getElementById("uiSquare_total").value;
  var buildingType = getBuildingType();
  var objectType = getObjectType();
  var rooms = parseInt(document.getElementById("uiRooms").value);
  var level = parseInt(document.getElementById("uiLevel").value);
  var levels = parseInt(document.getElementById("uiLevels").value);
  var kitchen_square = parseFloat(document.getElementById("uiSquare_kitchen").value);
  var region = parseInt(document.getElementById("uiLocations").value);
  var estPrice = document.getElementById("uiEstimatedPrice")

  var url = 'http://localhost:5000/predict_home_price' //-> local
  //var url = "/predict_home_price";

  $.post(url, {
    region: region,
    building_type: buildingType,
    level: level,
    levels: levels,
    rooms: rooms,
    area: parseFloat(area),
    kitchen_area: kitchen_square,
    object_type: objectType
  }, function(data, status) {
    console.log("Response data:", data);
    var estPrice = document.getElementById("uiEstimatedPrice");
    if (estPrice) {
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + "</h2>";
    } else {
      console.error("Element uiEstimatedPrice not found");
    }
    console.log("Status:", status);
  });

  
}
function onPageLoad() {
  console.log( "document loaded" );
  var url = "http://127.0.0.1:5000/get_location_names"; // local
  //var url = "/get_location_names"; // docker
  $.get(url,function(data, status) {
      console.log("got response for get_location_names request");
      if(data) {
          var locations = data.locations;
          var uiLocations = document.getElementById("uiLocations");
          //$('#uiLocations').empty();
          for(var i in locations) {
              var opt = new Option(locations[i]);
              $('#uiLocations').append(opt);
          }
      }
  });
}
// Привязка обработчика по id кнопки после загрузки страницы
window.onload = onPageLoad;

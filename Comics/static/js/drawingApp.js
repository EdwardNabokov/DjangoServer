/**
 * Created by Edward on 4/22/2017.
 */

var colorPurple = "#cb3594";
var colorGreen = "#659b41";
var colorYellow = "#ffcf33";
var colorBrown = "#986928";

var curColor = colorGreen;
var curSize = "large"; //small normal large huge


$(document).ready(function() {
  $('#colorPicker').change(function () {
    if ($('#colorPicker').val()) {
      pickColor(document.getElementById('colorPicker').value);
    }
  });
});


function pickColor(color){
  curColor = color;
}


canvas = document.getElementById('canvasDiv');


if(typeof G_vmlCanvasManager != 'undefined') {
    canvas = G_vmlCanvasManager.initElement(canvas);
}

context = canvas.getContext('2d');


$('#canvasDiv').mousedown(function(e) {
  var mouseX = e.pageX - this.offsetLeft;
  var mouseY = e.pageY - this.offsetTop;
  paint = true;
  addClick(e.pageX - this.offsetLeft, e.pageY - this.offsetTop);
  redraw();
});

$('#canvasDiv').mousemove(function(e){
  if(paint){
    addClick(e.pageX - this.offsetLeft, e.pageY - this.offsetTop, true);
    redraw();
  }
});

$('#canvasDiv').mouseup(function(e){
  paint = false;
});

$('#canvasDiv').mouseleave(function(e){
  paint = false;
});

var clickX = new Array();
var clickY = new Array();
var clickDrag = new Array();
var clickSize = new Array();
var clickColor = new Array();
var paint;

function addClick(x, y, dragging)
{
  clickX.push(x);
  clickY.push(y);
  clickDrag.push(dragging);
  clickColor.push(curColor);
  clickSize.push(curSize);
}


function redraw(){
  // context.clearRect(0, 0, context.canvas.width, context.canvas.height); // Clears the canvas

  context.lineJoin = "round";
  /* context.lineWidth = 5; */
  for(var i=0; i < clickX.length; i++)
  {
    context.beginPath();
    if(clickDrag[i] && i){
      context.moveTo(clickX[i-1], clickY[i-1]);
    }else{
      context.moveTo(clickX[i]-1, clickY[i]);
    }
    context.lineTo(clickX[i], clickY[i]);
    context.closePath();
    context.strokeStyle = clickColor[i];
    context.lineWidth = 25;
    context.stroke();
  }
}
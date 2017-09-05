function changeColor(o){

    o.style.backgroundColor = o.style.backgroundColor == paletteColor ? '#AAA' : paletteColor;

    }


function setPalette(o) {

    paletteColor = o.style.backgroundColor;
    currentPaletteDiv.style.backgroundColor = paletteColor;

}


window.onload = function () {

  paletteColors = ['red', 'blue', 'yellow', 'green'];
  paletteColor = paletteColors[0];
  gridContainer = document.getElementById('gridcontainer');
  palettesDiv = document.getElementById('palettes');

  for (i=0; i<100; i++) {
  
    box = document.createElement('div');
    box.className = 'griditem';

    box.addEventListener('click', function () {

         changeColor(this);

    });

    box.style.marginRight = '4px';
    gridContainer.appendChild(box);

  }

  for (colorIndex in paletteColors) {

    paletteElement = document.createElement('div');
    paletteElement.className = 'palette';
    paletteElement.style.backgroundColor = paletteColors[colorIndex];
    paletteElement.addEventListener('click', function () {

      setPalette(this);

});

    palettesDiv.appendChild(paletteElement);

}

  currentPaletteDiv = document.getElementById('current-palette')
  currentPaletteDiv.style.backgroundColor = paletteColor;
  

}

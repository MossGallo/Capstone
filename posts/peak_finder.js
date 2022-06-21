function commandscallback(cmd) {
  console.log('command: '+ cmd)
}

window.onload = () => {
  
  if (PeakFinder.utils.caniuse()) {

    let panel = new PeakFinder.PanoramaPanel({
      canvasid: 'pfcanvas', 
      locale: 'en' // attach to canvas
    })

    panel.registerCommandsCallback(commandscallback)
    
    panel.init(function() {
      console.log('ready')
      
      panel.settings.distanceUnit(1) // use imperial (miles, feet) format
              
      panel.loadViewpoint(46.53722, 8.12610, 'Finsteraarhorn') // loads a viewpoint
  
      // animate to view
      panel.azimut(209.0, 2.0)
      panel.altitude(1.0, 1.0)
      panel.fieldofview(45.0, 2.0)
    });
  }
  else { // !caniuse
  
  }

}

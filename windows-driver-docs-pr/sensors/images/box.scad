wallThickness=14;
roofThickness=14;
cubeHeight=305;
cubeWidth=406;
cubeLength=406;
aperatureWidth=254;
aperatureLength=254; 

difference () {
  translate([0,0,0])
	cube ([cubeWidth,cubeLength,cubeHeight],center = true);
  union () {
    translate([0,0,roofThickness])
    cube ([aperatureWidth,aperatureLength,cubeHeight],center = true);
    translate([0,0,-roofThickness])
		cube ([cubeWidth-wallThickness,cubeLength-wallThickness,cubeHeight-roofThickness],center = true);
  }
}

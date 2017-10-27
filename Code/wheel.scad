

module axle() {
	translate([0,0,-500])
	cylinder(1000, 7.4, 7.5);
	}
	
module pulley() {
	
	cylinder(8, 40, 40);
}

pulley();
axle();
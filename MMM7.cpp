#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;

double z1(double x, double y1) {
	return x * exp(-x) - y1;
}

double z2(double x, double y2){
	return exp(-x) - x * exp(-x) - y2;
}
double Taylor1(double x, double y1, double y2, double h) {
	return y1 + h * (y2 + h/2*(z1(x, y1)+ y2));
}

double Taylor2(double x, double y1, double y2, double h) {
	return y2 + h* (z1(x, y1)+ h/2*(z2(x, y2) - z1(x, y1)));
}


int main() {
	double y1 = 1, y2 = 0, y1n=0, y2n=0, z1=1, z2=0, z1n=0, z2n=0, m=0, h=.02, x=0, e=.01;
	ofstream f("points.txt");
	f << " " << x << " " << y1 << " " << y2 << endl;
	int k = 1;
	while (k > 0) {
		k = 0;
		while (x >= 0 && x <= 2 && m>=0 && m<=2) {
			y1n = Taylor1(x, y1, y2, h);
			y2n = Taylor2(x, y1, y2, h);
			x += h;
			y1 = y1n;
			y2 = y2n;
			z1n = Taylor1(m, z1, z2, h/2);
			z2n = Taylor2(m, z1, z2, h/2);
			m += h/2;
			z1 = z1n;
			z2 = z2n;
			z1n = Taylor1(m, z1, z2, h / 2);
			z2n = Taylor2(m, z1, z2, h / 2);
			m += h / 2;
			z1 = z1n;
			z2 = z2n;
			if (abs(y1 - z1) >= e || abs(y2 - z2) >= e)
				k++;
		}
		h *= .5;
		cout << "shag=" << h << endl;
		cout << " pogr posl iter= " << y1 - z1 << "  " << y2 - z2 << endl;
		y1 = 1, y2 = 0, y1n = 0, y2n = 0, x = 0, z1 = 1, z2 = 0, z1n = 0, z2n = 0, m = 0;
	 }
	 while (x >= 0 && x <= 2) {
		 y1n = Taylor1(x, y1, y2, h);
		 y2n = Taylor2(x, y1, y2, h);
		 x += h;
		 y1 = y1n;
		 y2 = y2n;
		 f << x << " " << y1 << " " << y2 << endl;
	 }
	return 0;
}
#include<iostream>

using namespace std;

int main() {
	int mass, sumA = 0, sumB = 0;
	auto fuel = [] (int mass) {return max(0, mass / 3 - 2);};
	while (cin >> mass) {
		sumA += fuel(mass); 
		sumB += fuel(mass);
		while (mass) 
			sumB += fuel(mass = fuel(mass));
	} 
	cout << "A: " << sumA << endl;
	cout << "B: " << sumB << endl;
	return 0;
}

#include <string>
#include <iostream>

using namespace std;

int main()
{
	string a;
	cin >> a;

	if (a == "a")
	{
		cin >> a;
		if (a == "b")
		{
			cout << "ab" << endl;
			abort();
		}
		if (a == "c")
		{
			cout << "other" << endl;
			abort();
		}
	}

	return 0;
}

// #include <string>
// #include <iostream>

// using namespace std;

// int main()
// {
// 	string a;
// 	cin >> a;

// 	if (a == "a")
// 	{
// 		abort();
// 	}

// 	return 0;
// }
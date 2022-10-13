
#include <iostream>
using namespace std;

int main()
{
    int n, t1 = 0, t2 = 1, next_term = 0;
    cout << "\nEnter the number of terms: ";
    cin >> n;
    cout << "\n";
    for (int i = 1; i <= n; ++i)
    {
        if (i == 1)
        {
            cout << i << "\t" << t1 << "\n";
            continue;
        }
        if (i == 2)
        {
            cout << i << "\t" << t2 << "\n";
            continue;
        }
        next_term = t1 + t2;
        t1 = t2;
        t2 = next_term;
        cout << i << "\t" << next_term << "\n";
    }
    cout << "\n[C++]\n\n";
    return 0;
}

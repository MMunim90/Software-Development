#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n; cin >> n;
    long long int arr[n];

    arr[1] = 0;
    arr[2] = 1;

    long long int sum = 0;

    for(int i=3; i<=n; i++)
    {
        arr[i] = arr[i-1] + arr[i-2];
        sum = arr[i];
    }

    cout << sum << endl;
    return 0;
}
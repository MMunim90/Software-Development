#include<bits/stdc++.h>
using namespace std;
int main()
{
    int a, b; cin >> a >> b;
    string s; cin >> s;

    if(s[a+1] != '-')
    {
        cout << "No" << endl;
        return 0;
    }

    bool wrong_code = false;

    for(int i=0; i<=s.size(); i++)
    {
        if(!(s[i] >= '0' && s[i] <= '9'))
        {
            wrong_code = true;
            break;
        }
    }

    if(wrong_code) cout << "No" << endl;
    else cout << "Yes" << endl;
    return 0;
}
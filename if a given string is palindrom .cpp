#include<bits\stdc++.h>
using namespace std;
int main()
{
    string a;
    int cf=0;
    cin>>a;
    for(int i=0,j=a.size()-1;i<a.size()&&j>=0;i++,j--)
    {
        if(a[i]==a[j])
        {
            cf++;
        }
    }
    if(cf==a.size())
    {
        cout<<"palindrom";
    }
    else
    {
        cout<<"not palindrom";
    }
    

    

}
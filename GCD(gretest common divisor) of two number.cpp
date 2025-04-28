#include<bits\stdc++.h>
using namespace std;
int main()
{
    int a,b,gcd;
    cin>>a>>b;
    int minv=min(a,b);
    for(int i=1;i<=minv;i++)
    {
        if(a%i==0 && b%i==0)
        {
          gcd=i;
          
        }
    }
    cout<<gcd;
    
} 

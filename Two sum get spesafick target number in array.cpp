#include<iostream>
using namespace std;
int main()
{
    int a[4]={1,2,3,4};
    int n,x1,cf,sum=0;
    cin>>n;
    for(int i=0;i<4;i++)
    {
     x1 =a[i];
     for(int i=i+1;i<4;i++)
     {
        sum=x1+a[i];
        if(sum==n)
        { 
          cf++;
          
        }
      }
     }
     if(cf>0)
     cout<<"Yes";
     else
     cout<<"No";
    return 0
}
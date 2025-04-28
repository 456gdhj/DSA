#include<bits\stdc++.h>
using namespace std;
int main()
{
    int a[]={1,3,4,7,8,4,3,9};
    int n=8;
    
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)

        { 
            if(i!=j && a[i]==a[j])
          {
            a[j]=-9;
         }

        }
    }
    for(int i=0;i<n;i++)
    {
        if(a[i]!=-9)
        {
            cout<<a[i];
        }
    }
}
#include<iostream>
using namespace std;

int main()
{
    int a[10],sum=0,i;
    
    cout<<"Enter ten number ";
    
    for(i=0;i<10;i++)
    { 
        cin>>a[i];
    }
    for(i=0;i<10;i++)
    {
        sum= sum + a[i];
    }
   cout<<"The sum of number "<<sum;
}
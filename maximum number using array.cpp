#include<iostream>
using namespace std;
int main()
{ 
    int a[100],i,n,maximum;
    cout<<"How many number you want ";
    cin>>n;
    cout<<"Enter number ";
    for(i=0;i<n;i++)
    {
        cin>>a[i];
    }
    maximum=0;
   for(i=0;i<n;i++)
   {
     
     if(maximum<a[i])
     maximum=a[i];
    }
   cout<<"The maximum number is "<<maximum;


}
#include<iostream>
using namespace std;
int main()
{
  int a[20],i,n;
 cout<<"How many number you want";
 cin>>n;
 a[0]=0;
 a[1]=1;
 for(i=2;i<n;i++)
 {
    a[i]=a[i-2]+a[i-1];
 }
 cout<<"Fibonaki seris ";
 for(i=0;i<n;i++)
 {
    cout<<a[i];
 }
}


#include<iostream>
using namespace std;
#include <math.h>
int main()
{
int n,x,result;
cout<<"Enter base number";
cin>>n;
cout<<"Enter power of number";
cin>>x;
result=pow(n,x);
cout<<result;
return 0;
}
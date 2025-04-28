#include<iostream>
using namespace std;

int prime(int n)
{
 int i,cf=0;

 for(i=1;n>=i;i++)
  {
    if(n%i==0)
    cf++;
    if(cf>2)
    break;

  }
 if(cf==2)
 cout<<"The number is prime";
 else
 cout<<"The number is not prime";
}

int main()
{
 int n;
 cout<<"Enter any number";
 cin>>n;
 prime(n);
 return 0;
}
#include<iostream>
using namespace std;
int main()
{
int n1,n2,x,i;

cout<<"Enter lowest number";

cin>>n1;
cout<<"Enter largest number";
cin>>n2;
for(i=n1+1;i<n2;i++)
{
    for(x=2;i>x;x++)
{
if(i%x==0)
break;

}
if(i==x)
cout<<i<<endl;
}
return 0;
}
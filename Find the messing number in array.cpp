#include<iostream>
using namespace std;
int main()
{
    int a[5]={1,2,3,4,5};
    int a1[6];int sum2=0,sum1=0,x;
    for(int i=0;i<6;i++)
    {
        cin>>a1[i];
        sum1=sum1+a1[i];

    }
    for(int i=0;i<5;i++)
    {
        sum2=sum2+a[i];
    }
    x=sum1-sum2;
    cout<<x<<endl;
    return 0;


}
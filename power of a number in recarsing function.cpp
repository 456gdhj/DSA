#include<iostream>
using namespace std;

int power(int n,int x)
{
    if(x>0)
    return (n*power(n,x-1));

    else 
    return 1;
    
}


int main()
{
    int n,x,result;
    cout<<"Enter any base";
    cin>>n;
    cout<<"Enter power of a number";
    cin>>x;
    result=power(n,x);
    cout<<"Power of number "<<result;
    return 0;
}






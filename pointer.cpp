#include<bits\stdc++.h>
using namespace std;
int main()
{
    int a[]={2,3,4,9,8};
    int*p=a;
    for(int i=0;i<5;i++)
    {
        cout<<*(p-1);
    }
}
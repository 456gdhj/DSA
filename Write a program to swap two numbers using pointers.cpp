#include<bits\stdc++.h>
using namespace std;
void swap(int *ptr1,int *ptr2)
{
 int temp;
 temp=*ptr1;
 *ptr1=*ptr2;
 *ptr2=temp;
}
int main()
{
 int x=10,y=20;
 swap(&x,&y);
 cout<<x<<endl;
 cout<<y<<endl;
}
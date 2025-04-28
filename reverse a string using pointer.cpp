#include<bits\stdc++.h>
using namespace std;
int main()
{
   char s[15];
   cout<<"Enter the string ";
   char *p=s;
   cin>>s;
   for(;*p!='\0';p++);
  
   for(;p>=s;p--)
   {
    cout<<*p;
   }


}
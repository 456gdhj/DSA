#include<bits\stdc++.h>
using namespace std;
int main()
{
    int cf=0;
    cout<<"Enter the string ";
   string s;
   cin>>s;
   for(int i=0;i<s.size();i++)
   {
    if(s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u')
    {
        cf++;
    }

   }
    cout<<cf;
}


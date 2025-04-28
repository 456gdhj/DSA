#include<bits\stdc++.h>
using namespace std;
int main()
{
    int n[3][3];
    cout<<"Enter matrix ";
    for(int i=0;i<3;i++)
    {
        for(int j=0;j<3;j++)
        {
            
            cin>>n[i][j];

        }
    }
    for(int i=0;i<3;i++)
    {
        for(int j=0;j<3;j++)
        {
            
            cout<<n[j][i];

        }
        cout<<endl;
    }


}
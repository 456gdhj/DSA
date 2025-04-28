#include<iostream>
using namespace std;
int main()
{
    int a[2][2];int n;
    cout<<"Enter matricks ";
    
    for(int i=0;i<2;i++)
    {
        for(int j=0;j<2;j++)
        {
            cin>>a[i][j];
        }
    }
    cout<<"Enter expect number ";
    cin>>n;

    for(int i=0;i<2;i++)
    {
        for(int j=0;j<2;j++)
         {  
            if(a[i][j]==n)
             {
               cout<<"Row "<<i+1<<endl;
                cout<<"Colam "<<j+1;
                break;
             }
      }
    }
}
     
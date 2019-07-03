#include <iostream>

using namespace std;

int main()
{
    int a[1000][1000],a1,b1,c,d,i,j,co=0;
    cin>>a1;
    c=a1+2;
    for (i=0;i<c;i++)
    for (j=0;j<c;j++)
    {
        if ((i==0)||(i==c-1)||(j==0)||(j==c-1))
        a[i][j]=0;
    }
    for(i=1;i<=a1;i++)
    for(j=1;j<=a1;j++)
    cin>>a[i][j];
    /*for (i=0;i<c;i++)
    {
        for(j=0;j<c;j++)
        {
            cout<<a[i][j]<<"\t";
        }
        cout<<"\n";
    }*/
    for(i=1;i<=a1;i++)
    {
        for(j=1;j<=a1;j++)
        {
            if((a[i][j]==1 && a[i-1][j]==0 && a[i+1][j]==0 && a[i][j-1]==0 && a[i][j+1]==0 && a[i-1][j-1]==0 && a[i+1][j-1]==0 && a[i+1][j+1]==0 && a[i-1][j+1]==0))
            {
            co++;
            }
        }
    }
    cout<<co;
    return 0;
}

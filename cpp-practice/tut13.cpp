#include<iostream>
using namespace std;

int main(){
    int marks[] = {24,57,63,78,98,45,57};
    int num = 0;

    int* p = marks;

    cout<<*(p++)<<endl;
    cout<<*(++p)<<endl;

    /*while (num <= sizeof(arr) - 1) {
        cout<<arr[num]<<endl;
        num++;
    }*/
    
    return 0;
}
#include<iostream>

using namespace std;

int main() {
    int age;
    cout<<"Enter Your Age:"<<endl;
    cin>>age;
    if (age<18) {
        cout<<"You are not allowed..."<<endl;
    }
    else if (age==18) {
        cout<<"You will get a kid licence..."<<endl;
    }
    else{
        cout<<"You are allowed..."<<endl;
    }
    return 0;
}
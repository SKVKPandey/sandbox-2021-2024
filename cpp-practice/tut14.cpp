#include<iostream>
using namespace std;

struct DataSet {
    string name;
    int roll;
};

int main(){
    struct DataSet Student1;
    Student1.name = "Shashank Kashyap";
    cout<<Student1.name<<endl;
    return 0;
}
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int n=3;
vector<char>  chs= {'a','b','c'};
vector<char> cur_chs(3);
vector<char> cur(3);


bool constraint(vector<char>& cur_chs, char c)
{
    int num=0;
    for(int j = 0;j<cur_chs.size();j++)
    {
        if(cur_chs[j]==c)
            num++;
            return false;
    }
    return true;
}

void backtrack(int t)
{
    if(t>=n){
        for(char& c : cur_chs){
            cout<<c;
        }
        cout<<endl;
    }else{
        for(char&c :  chs){
            if(constraint(cur_chs,c)){
                cur_chs[t] = c;
                backtrack(t+1);
                cur_chs[t] = ' ';
            }
        }


    }
}


int main() {
    backtrack(0);
    return 0;
}

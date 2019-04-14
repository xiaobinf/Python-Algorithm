#include <iostream>
#include <vector>
using namespace std;
int c =12,n=5;
vector<int> weight = {2,2,6,5,4};
vector<int> value = {6,3,5,4,6};
int curV = 0,curW = 0;
int bestV = 0;
vector<int> x(5,0);
vector<int> bestx(5,0);
vector<int> range = {0,1};
bool consraint(int t, int i)
{
    if(weight[t]*i+curW <= c) {
        return true;
    }
    return false;
}

void backtrack(int t)
{
    if(t>=n){
        if(curV>bestV){
            bestV = curV;
            bestx = x;
        }
    }else{
        for(int&i :  range){
            x[t] = i;
            if(consraint(t,i)){
                curW += weight[t]*i;
                curV += value[t]*i;
                backtrack(t+1);
                curW -= weight[t]*i;
                curV -= value[t]*i;
            }
        }
    }
}


int main() {
    backtrack(0);
    for(int i: bestx){
        cout<<i<<endl;
    }
    cout<<endl<<bestV<<endl;
    return 0;
}
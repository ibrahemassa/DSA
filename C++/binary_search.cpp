#include <iostream>
#include <vector>

using namespace std;

int b_search(vector<int> arr, int target){
    int l = 0, r = arr.size() - 1;
    while (l <= r){
        int mid = (l + r) / 2;
        if (arr[mid] < target){
            l = mid + 1;
        }
        else if (arr[mid] > target){
            r = mid - 1;
        }
        else if (arr[mid] == target){
            return mid;
        }
    }
    return -1;
}

int main(){
    vector<int> x = {1,2,4,6,22,36,42,77};
    int target;
    cout<<"Enter a number to search in the array: ";
    cin>>target;
    cout<<b_search(x, target)<<endl;
    return 0;
}
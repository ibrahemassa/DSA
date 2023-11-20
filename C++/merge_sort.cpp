#include <iostream>
#include <vector>

using namespace std;

void merge(vector<int>& left, vector<int>& right, vector<int>& arr){
    int i = 0, l = 0, r = 0;
    while (l < left.size() && r < right.size()){
        if (left[l] < right[r])
            arr[i++] = left[l++];
        else
            arr[i++] = right[r++];
    }
    while (l < left.size())
        arr[i++] = left[l++];
    while (r < right.size())
        arr[i++] = right[r++];
}

void merge_sort(vector<int>& arr, int length){
    int l = 0, m = (length+l)/2;
    if (length <= 1)
        return;
    vector<int> left, right;
    for (int i = 0; i < length; i++){
        if (i < m)
            left.push_back(arr[i]);
        else
            right.push_back(arr[i]);
    }
    merge_sort(left, left.size());
    merge_sort(right, right.size());
    merge(left, right, arr);
}

int main(){
    vector<int> x = {6,2,8,3,1,9};
    merge_sort(x, x.size());
    
    for (int i = 0; i < x.size(); i++){
        cout<<x[i]<<", ";
    }
    cout<<endl;
}
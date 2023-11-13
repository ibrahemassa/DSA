#include <iostream>

using namespace std;

void bubble_sort(int arr[], int size){
    for (int i = 0; i < size; i++)
        for (int j = 0; j < size - 1 - i; j++){
            if(arr[j] > arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
}

int main(){
    int x[] = {6,3,8,22,5,4,99,21};
    int size = sizeof(x)/sizeof(int);
    bubble_sort(x, size);

    for (int i = 0; i < size; i++)
        cout<<x[i]<<endl;
    return 0;
}
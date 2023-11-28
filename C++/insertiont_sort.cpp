#include<iostream>

void insertion_sort(int [], int);

int main(){
    int x[] = {5, 2, 6, 3, 4, 1, 20, 0, 9, 12};
    int size = sizeof(x)/sizeof(int);
    insertion_sort(x, size);
    std::cout<<"Sorted array: ";
    for (int i = 0; i < size; i++)
        std::cout<<x[i]<<", ";
    return 0;
}

void insertion_sort(int arr[], int size){
    for (int i = 0; i < size; i++)
    {
        int key = arr[i], j = i - 1;

        while (j >= 0 && key < arr[j]){
            arr[j+1] = arr[j];
            j -= 1;
        }

        arr[j+1] = key;        
    }
}
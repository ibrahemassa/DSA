#include<iostream>

int partition(int [], int, int);
void quick_sort(int [], int, int);

int main(){
    int x[] = {5, 2, 6, 3, 4, 1, 20, 3};
    int size = sizeof(x)/sizeof(int);
    quick_sort(x, 0, size-1);
    std::cout<<"Sorted array: ";
    for (int i = 0; i < size; i++)
        std::cout<<x[i]<<", ";
    return 0;
}

int partition(int arr[], int l, int r){
    int pivot = arr[l];
    int great = l+1, less = r;

    while(true){
        while (great <= r && arr[great] < pivot)
            great++;
        
        while (less >= l && arr[less] > pivot)
            less--;
        
        if(great < less){
            int temp = arr[less];
            arr[less] = arr[great];
            arr[great] = temp;
        }
        else
            break;
    }
    arr[l] = arr[less];
    arr[less] = pivot;
    
    return less;
}

void quick_sort(int arr[], int l, int r){
    if (r - l <= 0)
        return;
    int point = partition(arr, l, r);
    quick_sort(arr, l, point-1);
    quick_sort(arr, point+1, r);
}

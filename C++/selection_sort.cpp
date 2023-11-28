#include <iostream>

void selection_sort(int [], int);

int main(){
    int x[] = {5, 2, 6, 3, 4, 1, 20};
    int size = sizeof(x)/sizeof(int);
    selection_sort(x, size);
    std::cout<<"Sorted array: ";
    for (int i = 0; i < size; i++)
        std::cout<<x[i]<<", ";
    return 0;
}

void selection_sort(int arr[], int size){
    for (int i = 0; i < size; i++)
    {
        int min = i;

        for (int j = i+1; j < size; j++)
            if (arr[j] < arr[min])
                min = j;

        int temp = arr[i];
        arr[i] = arr[min];
        arr[min] = temp;
    }
}

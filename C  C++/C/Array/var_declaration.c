#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    // Cách 1 : Khai báo trước nhập giá trị sau
    int arr1[3];
    arr1[0] = 1;
    arr1[2] = 1;
    arr1[3] = 1;

    // Cách 2 vừa khai báo vừa khởi tạo
    char name[] = "Nguyen Quang Tiep";
    float snt[] = {1,2,3,4,5};

    // Khai báo dùng con trỏ
    int *myArray;
    int size = 5;
    myArray = (int *)malloc(size * sizeof(int));

    // printf arr1
    
    
    return 0;
}

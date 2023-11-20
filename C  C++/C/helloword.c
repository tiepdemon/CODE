#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "abcdefghi";
    
    // Di chuyển chuỗi "defghi" đến phía trước
    memmove(str + 3, str + 6, 3);
    
    printf("Chuỗi sau khi di chuyển: %s\n", str);
    
    return 0;
}

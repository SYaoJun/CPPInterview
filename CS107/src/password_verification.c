#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool verifyPassword(char *password, char *validChars, char *badSubstrings[], size_t count){
    int n = strlen(password);
    // 返回一个整数，如果前一个字符串中的字符都出现在后一个字符串中，则返回值为前一个字符串的长度
    if(strspn(password, validChars) != n){
        return false;
    }
    for(int i = 0; i < count; i++) {
        // 找到第一个字符串匹配的位置
        if(strstr(password, badSubstrings[i]) != NULL) {
            return false;
        }
    }
    return true;
}
int main() {
    char *invalidSubstrings[] = { "1234" , "4132"};
    bool valid1 = verifyPassword("1572", "0123456789",
                                 invalidSubstrings, 2);
    printf("%s\n", valid1?"true":"false");
    bool valid2 = verifyPassword("141234", "0123456789",
                                 invalidSubstrings, 2);
    printf("%s\n", valid2?"true":"false");
    return 0;

}
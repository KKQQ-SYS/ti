#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main(void) {
    double s[3]; // 使用double支持小数边长
    int i;

    // 1. 输入循环
    for (i = 0; i < 3; i++) {
        printf("请输入第 %d 条边: ", i + 1);
        if (scanf("%lf", &s[i]) != 1 || s[i] <= 0) {
            printf("错误：请输入大于0的有效数字。\n");
            return EXIT_FAILURE; 
        }
    }

    // 2. 三角形合法性检查
    if (!(s[0] + s[1] > s[2] && s[0] + s[2] > s[1] && s[1] + s[2] > s[0])) {
        printf("这三条边无法组成三角形。\n");
        return 0;
    }

    printf("这是一个：");

    // 3. 属性判断（使用独立判断或更严谨的嵌套）
    bool isEquilateral = (s[0] == s[1] && s[1] == s[2]);
    bool isIsosceles = (s[0] == s[1] || s[0] == s[2] || s[1] == s[2]);
    
    // 直角判定（考虑浮点数误差，实际开发中通常使用 epsilon 比较）
    bool isRight = (s[0]*s[0] + s[1]*s[1] == s[2]*s[2] || 
                    s[0]*s[0] + s[2]*s[2] == s[1]*s[1] || 
                    s[1]*s[1] + s[2]*s[2] == s[0]*s[0]);

    if (isEquilateral) {
        printf("等边三角形");
    } else if (isIsosceles) {
        printf("等腰三角形");
    } else {
        printf("普通三角形");
    }

    if (isRight) {
        printf(" 且是 直角三角形");
    }

    printf("\n");
    return 0;
}
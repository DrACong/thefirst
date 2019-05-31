#include <stdio.h>
int main(){
    float mile=-1.0;
    int time=-1;
    int cost=-1;
    scanf("%f%d", &mile, &time);
    if(mile<=3)
        cost = (int)(10+time/5*2+0.5); 
        // 浮点数结果加0.5结合强转即可四舍五入
    else if(mile<=10)
        cost = (int)(10+(mile-3)*2+time/5*2+0.5);
    else
        cost = (int)(10+7*2+(mile-10)*3+time/5*2+0.5);
    printf("%d\n", cost);

    return 0;
}

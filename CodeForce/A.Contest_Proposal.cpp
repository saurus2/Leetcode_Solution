#include <iostream>
using namespace std;

int main(){
    int t = 0;
    scanf("%d", &t);
    while(t--){
        int n = 0;
        int ans = 0;
        scanf("%d", &n);
        int a[n], b[n];
        for(int i = 0; i < n; i++){
            scanf("%d", &a[i]);
        }
        for(int i = 0; i < n; i++){
            scanf("%d", &b[i]);
        }
        int p_a = 0;
        int p_b = 0;
        while(p_b < n){
            if(a[p_a] <= b[p_b]){
                p_a++;
                p_b++;
            }else{
                p_b++;
                ans++;
            }
        }
        printf("%d\n", ans);
    }
}